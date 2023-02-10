frase = 'Curso em Video Python'

#FATIAR
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#ANÁLISE
print(len(frase)) # ler quantos caracteres tem a string
print(frase.count('o')) # ler quantos caracteres especificos tem na string
print(frase.count('o',0,13))
print(frase.find('deo')) # vai encontrar onde inicia os caracteres
print(frase.find('Android')) # retorna -1 significando que não foi encontrado
print('Curso' in frase) # existe a palavra na frase

#TRANSFORMAÇÃO
print(frase.replace('Python','Android')) # substituir palavra ou frase
print(frase.upper()) # deixar tudo em maiúscula
print(frase.lower()) # deixa em minúscula
print(frase.capitalize()) # apenas primeiro caractere em maiúscula
print(frase.title()) # primeira letra de cada palavra em maiúscula

frase2 = '   Aprenda Python  '

print(frase2.strip()) # remove os espaços
print(frase2.rstrip()) # r = right(direita) remove os espaços da direita
print(frase2.lstrip()) # l = left(esquerda) remove espaços da esquerda

#DIVISÃO
print(frase.split()) # gera uma lista de palavras, cada palavra inicia de 0, e cada pedaço gera uma numeração

#JUNÇÃO
print('-'.join(frase))


print("""Sou admirador da tecnologia e pelo que ela nos proporciona. O que gosto na tecnologia é a possibilidade de 
constante inovação, presenciar os resultados imediatos das ferramentas e funcionalidades desenvolvidas.
Utilizo da CURIOSIDADE e CRIATIVIDADE para desenvolver meus projetos, para obter o melhor resultado.""") # para strings grandes usar """

print(frase.upper().count('O')) # juntar comandos



