texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("Executa no final do laço")


# FOR com RANGE
for numero in range(0, 51, 5):
    print(numero, end=" ")