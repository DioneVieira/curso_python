import datetime

# PACOTE DATATIME
''' O datetime módulo fornece classes para manipulação de datas e horas '''

print(type('31/05/2023'))

dia_hoje = datetime.datetime.today()
print(dia_hoje)
print(type(dia_hoje))

print(datetime.datetime.today().date())
data = datetime.datetime.today().date()
ano = data.year
mes = data.month
dia = data.day

print(ano, mes, dia)

data_antiga = datetime.date(2022, 1, 1)
print(data_antiga)

print(data - data_antiga)

# mudar formato
print(data.strftime('%d/%m/%y'))

print(data + datetime.timedelta(days=30))
