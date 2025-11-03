from typing import List, Dict, Optional

# ----------------------------- Dados Globais ----------------------------- #
clientes: List[Dict] = []
contas: List[Dict] = []
AGENCIA = "0001"
proximo_numero_conta = 1
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500.0

# ----------------------------- Menu ----------------------------- #
def menu() -> str:
    return """
[nu] Novo cliente
[nc] Nova conta
[lc] Listar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# ----------------------------- Clientes ----------------------------- #
def filtrar_cliente(cpf: str) -> Optional[Dict]:
    return next((c for c in clientes if c["cpf"] == cpf), None)

def criar_cliente() -> None:
    cpf = input("CPF: ").strip()
    if filtrar_cliente(cpf):
        print("Cliente já existe!")
        return
    nome = input("Nome: ").strip()
    data_nasc = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Endereço: ").strip()
    clientes.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nasc,
        "endereco": endereco
    })
    print("Cliente criado com sucesso!")

# ----------------------------- Contas ----------------------------- #
def criar_conta() -> None:
    global proximo_numero_conta
    cpf = input("CPF do cliente: ").strip()
    cliente = filtrar_cliente(cpf)
    if not cliente:
        print("Cliente não encontrado!")
        return
    conta = {
        "agencia": AGENCIA,
        "numero": proximo_numero_conta,
        "cliente_cpf": cpf,
        "saldo": 0.0,
        "extrato": "",
        "saques": 0
    }
    contas.append(conta)
    proximo_numero_conta += 1
    print(f"Conta criada para {cliente['nome']} - Conta {conta['numero']}")

def listar_contas() -> None:
    if not contas:
        print("Não há contas cadastradas")
        return
    for c in contas:
        cliente = filtrar_cliente(c["cliente_cpf"])
        print(f"Agência: {c['agencia']} | Conta: {c['numero']} | Cliente: {cliente['nome']}")

def selecionar_conta() -> Optional[Dict]:
    cpf = input("CPF do titular: ").strip()
    contas_cliente = [c for c in contas if c["cliente_cpf"] == cpf]
    if not contas_cliente:
        print("Cliente não possui contas")
        return None
    if len(contas_cliente) == 1:
        return contas_cliente[0]
    print("Contas do cliente:")
    for c in contas_cliente:
        print(f"- Conta {c['numero']} (Agência {c['agencia']})")
    try:
        numero = int(input("Número da conta: "))
    except ValueError:
        print("Conta inexistente")
        return None
    return next((c for c in contas_cliente if c["numero"] == numero), None)

# ----------------------------- Operações ----------------------------- #
def depositar(conta: Dict) -> None:
    try:
        valor = float(input("Valor a depositar: "))
        if valor <= 0:
            print("Valor inválido")
            return
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado")
    except ValueError:
        print("Valor inválido")

def sacar(conta: Dict) -> None:
    try:
        valor = float(input("Valor a sacar: "))
    except ValueError:
        print("Valor inválido")
        return
    if valor > conta["saldo"]:
        print("Saldo insuficiente")
    elif valor > LIMITE_SAQUE_VALOR:
        print("Valor excede o limite")
    elif conta["saques"] >= LIMITE_SAQUES:
        print("Limite de saques atingido")
    elif valor <= 0:
        print("Valor inválido")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["saques"] += 1
        print("Saque realizado")

def exibir_extrato(conta: Dict) -> None:
    print("\n=== EXTRATO ===")
    print(conta["extrato"] if conta["extrato"] else "Nenhuma movimentação")
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("================")

# ----------------------------- Fluxo principal ----------------------------- #
def main() -> None:
    while True:
        opcao = input(menu()).strip().lower()
        if opcao == "nu":
            criar_cliente()
        elif opcao == "nc":
            criar_conta()
        elif opcao == "lc":
            listar_contas()
        elif opcao == "d":
            conta = selecionar_conta()
            if conta: depositar(conta)
        elif opcao == "s":
            conta = selecionar_conta()
            if conta: sacar(conta)
        elif opcao == "e":
            conta = selecionar_conta()
            if conta: exibir_extrato(conta)
        elif opcao == "q":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()