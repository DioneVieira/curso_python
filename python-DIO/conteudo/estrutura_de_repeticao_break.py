while True:
    numero = int(input("Informe um número:"))

    if numero == 10:
        break

    print(numero)

# BREAK = Parar
for numero in range(100):

    if numero == 12:
        break

    print(numero, end=" ")

# Continue
for numero in range(100):

    if numero == 12:
        continue

    print(numero, end=" ")