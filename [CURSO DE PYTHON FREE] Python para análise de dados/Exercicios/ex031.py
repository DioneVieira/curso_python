# 31ª Exercício ###

# Utilize o módulo datetime e mostre na tela a data e hora atual do sistema de acordo com o formato descrito abaixo.

import datetime

data_atual = datetime.datetime.now()
print(data_atual.strftime('%d/%m/%Y - %H:%M:%S'))
