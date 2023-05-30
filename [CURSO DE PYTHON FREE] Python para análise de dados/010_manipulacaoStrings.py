#MANIPULAÇÃO DE STRINGS
'''
Um tipo de dados bastante usado no dia a dia são as strings, ou cadeias de caracteres (ou sequências de caracteres).
O tipo de dados string, ou str como é chamado em Python, possui várias operações úteis associadas a ele.
Essas operações tornam Python uma linguagem bastante propícia para manipulação de textos. Algumas funções mais utilizadas:
'''

string = 'Olá Mundo!!'
print(len(string))
print(type(string))

print(string + ' Concatenei')
#1. replace() troca um dado por outro
print(string.replace('Mundo','World'))

#2. startswith() verifica o começo
print(string.startswith('Olá'))

#3. endswith() verifica o fim
print(string.endswith('Mundo!!'))

#4. count() conta um dado específico
print(string.count('o'))

#5. capitalize() coloca inicial maiúscula
nome = 'dione'
print(nome.capitalize())

#6. isdigit() verifica se são digitos
cpf = '123456789'
print(cpf.isdigit())

#7. isalnum() verifica se é número
print(string.isalnum())

#8. upper() deixa tudo maiúscula
print(string.upper())

#9. lower() deixa tudo minúscula
string_02 = 'DIONE'
print(string_02.lower())

#10. find () mostra onde começa o valor solicitado
frase = ' Desistir não é uma opção '
print(frase.find('não'))

#11. strip() remove espaços no começo é fim
print(frase)
print(frase.strip())

#12. split() cria uma lista conforme o parametro passado ao comando
endereco = 'Rua Aurélio Ultramari, Curitiba, PR'
print(endereco.split(' ')) # ',' '.' 'espaço'

