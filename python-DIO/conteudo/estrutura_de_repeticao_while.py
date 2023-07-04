opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Efetuando saque. Aguade...")
    elif opcao == 2:
        print("Imprimindo extrato. Aguarde...")
else:
    print("Obrigado por usar nosso banco. Até logo.")