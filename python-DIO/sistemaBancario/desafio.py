menu ='''
--------------------------------
Selecione uma das opções abaixo:

[1] Sacar
[2] Depositar
[3] Extrato
[0] Finalizar
--------------------------------
->
'''

LIMITE_SAQUE_DIARIO = 3
numero_saques = 0
saldo = 0
limite = 500
extrato = ""


while True:

    opcao = input(menu)

    if opcao == "1":
        print("Saque")
        valor = float(input("Qual o valor do saque que você deseja realizar: R$ "))

        sem_saldo = valor > saldo

        saque_exedito = numero_saques >= LIMITE_SAQUE_DIARIO

        limite_exedito = valor > limite

        if sem_saldo:
            print("Você não tem saldo o suficiente para realizar está operação.")

        elif saque_exedito:
            print("Operação não realizada! Você ja realizou os 3 saques diários dísponiveis.")

        elif limite_exedito:
            print("O valor solicitado é maior que o limite de saque permitido.\nSeu limite de saque atual é de R$500,00.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado R$ {valor:.2f}\n"
            numero_saques +=1

        else:
            print("Não foi possivel realizar a operação.\nDigite o valor a ser sacado.")

        

    elif opcao == "2":
        print("Depósito")
        valor = float(input("Qual o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito realizado: R$ {valor:.2f}\n"

        else:
            print("Não foi possível realizar a operação.\nDigite o valor a ser depositado.")

    elif opcao == "3":
        print("---------- EXTRATO DA CONTA ---------")
        print("Não foi realizada nenhuma movimentação na sua conta." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("------------------------------------")


    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços. Até logo.")
        break

    else:
        print("Opção inválida!\nPor favor selecione uma das opções a seguir.")