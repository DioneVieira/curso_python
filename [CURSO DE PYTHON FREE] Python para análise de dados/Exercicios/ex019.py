# 19ª Exercício ###

"""Escreva um programa que solicite o nome, o sobrenome e o salário atual de um funcionário. Ao fim, calcule seu novo
salário considerando cenários hipotéticos, com os seguintes aumentos: 10%, 25%,30% e 50%. A mensagem na tela deverá
seguir o seguinte padrão:

"Olá, [nome] [sobrenome]"

"Seu salário atual é : [salário]"

"Seu salário com 10% de aumento é: [salário]"

"Seu salário com 25% de aumento é: [salário]"

"Seu salário com 30% de aumento é: [salário]"

"Seu salário com 50% de aumento é: [salário]"

No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os
espaços antes e após a string, enquanto que o último permite colocar a string no formato titlecased
(capitaliza string)."""

nome = input('Digite seu nome: ').strip().title()
sobrenome = input('Digite seu sobrenome: ').strip().title()
salario = float(input('Digite seu salário: '))
salario1 = salario + salario * 0.1  # salário com 10% de aumento
salario2 = salario + salario * 0.25  # salário com 25% de aumento
salario3 = salario + salario * 0.3  # salário com 30% de aumento
salario4 = salario + salario * 0.5  # salário com 50% de aumento

print(f'Olá, {nome} {sobrenome}')
print(f'Seu salário atual é: R$ {salario:.2f}')
print(f'Seu salário com 10% de aumento é: R$ {salario1:.2f}')
print(f'Seu salário com 25% de aumento é: R$ {salario2:.2f}')
print(f'Seu salário com 30% de aumento é: R$ {salario3:.2f}')
print(f'Seu salário com 50% de aumento é: R$ {salario4:.2f}')
