import time
# Este módulo fornece várias funções relacionadas ao tempo

print('Comecei agora...')
time.sleep(2) # tempo para executar proxima informação
print('Terminei')

agora = time.localtime()
print(agora)
print(type(agora))

print(time.strftime('%d/%m/%y, %H:%M:%S', agora))

time_texto = '21 June, 2023'
print(time.strptime(time_texto, '%d %B, %Y'))