nome = "Dione"
idade = 30
profissao = "Analista de Dados"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Dione", "idade": 30}

print("Nome: %s idade: %d" % (nome, idade))

print("Nome: {} idade: {}".format(nome, idade))

print("Nome: {1} idade: {0}".format(idade, nome))
print("Nome: {1} idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} idade: {age} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} saldo: {saldo:10.2f}")