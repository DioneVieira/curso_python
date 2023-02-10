# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input("Nome do aluno: ")
print('='*100)
nota1 = float(input('1º nota: '))
nota2 = float(input('2º nota: '))
print('='*100)
print('O aluno {}, teve media {:.1f}.'.format(nome,((nota1+nota2)/2)))
p = 'PARABÉNS'
print('{:=^100}'.format(p))
