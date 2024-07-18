
# --------------------------------- 1ª VERSÃO -------------------------------- #

menu = """ 

[d] Depostitar
[s] Sacar
[e] Extrato
[q] Sair

=> """ # <- indica que o usuário deve inserir sua escolha

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3 # aqui é uma constante

while True:
    
    opcao = input(menu)
    
    if opcao == 'd': #somente valor posit, exibir no estrato
        valor_depositado = float(input("Informe o valor do depósito: "))
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito R${valor_depositado:.2f}\n"
        
    elif opcao == 's': #somente 3 saque, máximo de 500 por saque - caso sem sald exbiri mensagem de sem saldo-exibir no extrato
        if numero_saque >= LIMITE_SAQUES:
                print("Limite de saques atingido! Encerrando operações")
                break
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque > 0 and valor_saque < saldo and valor_saque <= limite:
            saldo -= valor_saque
            extrato += f"Saque R${valor_saque:.2f}\n"
            numero_saque += 1
        elif valor_saque > saldo:  # Verifica se o saldo é insuficiente
                print("Saldo insuficiente.")
        elif valor_saque > limite:  # Verifica se o valor excede o limite por operação
                print(f"Valor do saque excede o limite de R${limite:.2f} por operação.")
        else:
                print("Valor inválido. O saque deve ser um valor positivo.")
            
    elif opcao == 'e': #listar todas operações - no fim saldo deve ser exibido - valores exibidos em R$xxx.xx
        print("\nExtrato:") #\n significa uma quebra de linha
        
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas movimentações.")  # Mensagem se não houver operações
        print(f"\nSaldo atual: R${saldo:.2f}")  # Imprime o saldo atual
        
    elif opcao == 'q':
        print("Saindo do sistema")
        break
        
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
        
        
# --------------------------------- 2ª VERSÃO --------------------------------- #


# Otimização Projeto Sistema Bancário

# 1 - Separar em funções saque, depósito e extrato.
# 2 - Criar duas novas funções: cadastrar usuário(cliente) e cadastrar conta bancária(vincular com usuário)


# def menu(): 
#     menu = """\n 
# =============== MENU ===============
# [d]\tDepostitar
# [s]\tSacar
# [e]\tExtrato
# [nc]\tNova Conta
# [lc]\tLIstar Contas
# [nu]\tNovo Usuário
# [q]\tSair

# => """ # <- indica que o usuário deve inserir sua escolha
# # \t insere um espaço de tabulação, que é equivalente a pressionar a tecla Tab no teclado.
#     return input((menu))


# def main():
#     LIMITE_SAQUES = 3 # aqui é uma constante
#     AGENCIA = "0001"
    
#     saldo = 0
#     limite = 500
#     extrato = ""
#     numero_saque = 0
#     usuaruis = []
#     contas = []
    
#     while True:
    
#         opcao = (menu)
    
#         if opcao == 'd': #somente valor posit, exibir no estrato
#         valor_depositado = float(input("Informe o valor do depósito: "))
        
#         if valor_depositado > 0:
#             saldo += valor_depositado
#             extrato += f"Depósito R${valor_depositado:.2f}\n"
        
#         elif opcao == 's': #somente 3 saque, máximo de 500 por saque - caso sem sald exbiri mensagem de sem saldo-exibir no extrato
#         if numero_saque >= LIMITE_SAQUES:
#                 print("Limite de saques atingido! Encerrando operações")
#                 break
#         valor_saque = float(input("Digite o valor a ser sacado: "))
#         if valor_saque > 0 and valor_saque < saldo and valor_saque <= limite:
#             saldo -= valor_saque
#             extrato += f"Saque R${valor_saque:.2f}\n"
#             numero_saque += 1
#         elif valor_saque > saldo:  # Verifica se o saldo é insuficiente
#                 print("Saldo insuficiente.")
#         elif valor_saque > limite:  # Verifica se o valor excede o limite por operação
#                 print(f"Valor do saque excede o limite de R${limite:.2f} por operação.")
#         else:
#                 print("Valor inválido. O saque deve ser um valor positivo.")
            
#         elif opcao == 'e': #listar todas operações - no fim saldo deve ser exibido - valores exibidos em R$xxx.xx
#         print("\nExtrato:") #\n significa uma quebra de linha
        
#         if extrato:
#             print(extrato)
#         else:
#             print("Não foram realizadas movimentações.")  # Mensagem se não houver operações
#         print(f"\nSaldo atual: R${saldo:.2f}")  # Imprime o saldo atual

#         elif opcao == 'q':
#         print("Saindo do sistema")
#         break
        
    
#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada")