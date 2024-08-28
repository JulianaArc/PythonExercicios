nome = str(input('qual é o seu nome?')).strip()
if nome == 'gustavo':
    print('que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('belo nome feminino')
else:
    print('seu nome é bem normal.')
print('tenha um bom dia, {}!'.format(nome))

