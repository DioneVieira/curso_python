#Faça uma tabuada que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

print('Olá!!!')
num = int(input('A tabuada de qual número interio você deseja saber? '))
print('-'*12)
print('A tabuada do {} é:\n{} x  1 = {}'.format(num, num, num*1))
print('{} x  2 = {}\n{} x  3 = {}\n{} x  4 = {}\n{} x  5 = {}\n{} x  6 = {}'.format(num, num*2,num, num*3,num, num*4, num, num*5,num, num*6))
print('{} x  7 = {}\n{} x  8 = {}\n{} x  9 = {}\n{} x 10 = {}'.format(num, num*7, num, num*8, num, num*9,num, num*10))
print('-'*12)