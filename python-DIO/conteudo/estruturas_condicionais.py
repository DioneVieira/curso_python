saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque de R$", saque)

else:
    print("Você não tem saldo suficiente!!!\nSeu saldo atual é de R$", saldo)


