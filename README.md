#  Desafio - Sistema Bancário (DIO)

Projeto desenvolvido como parte do **Desafio da DIO** com foco em aprimorar o raciocínio lógico e a organização de um sistema bancário em Python.  

---

##  Funcionalidades

- Cadastro de clientes com **CPF, nome, data de nascimento e endereço**  
- Criação de **contas bancárias** vinculadas a clientes existentes  
- **Depósito** em conta  
- **Saque** com controle de:
  - saldo disponível  
  - limite de valor por saque (R$ 500,00)  
  - limite máximo de 3 saques diários  
- **Transferência entre contas** 🆕  
- **Extrato** com todas as movimentações realizadas  
- **Listagem de contas cadastradas**  
- Menu interativo com opções simples e diretas  

---

##  Melhorias em relação à v1
 
- **Funções otimizadas** para operações bancárias  
- Implementação da **função de transferência entre contas**  
- Mensagens mais claras e feedbacks aprimorados para o usuário  

---

##  Tecnologias utilizadas

- **Python 3**
- Estruturas de dados: *listas* e *dicionários*  
- Funções e controle de fluxo (*if/else*, *while*, *try/except*)  

---

##  Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/sistema-bancario-v2.git

   Acesse a pasta do projeto:
   cd sistema-bancario-v2

   Execute o programa:
   python banco_v2.py

   Use o menu interativo:
    [nu] Novo cliente  
    [nc] Nova conta  
    [lc] Listar contas  
    [d]  Depositar  
    [s]  Sacar  
    [t]  Transferir  
    [e]  Extrato  
    [q]  Sair  



