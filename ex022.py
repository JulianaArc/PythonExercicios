nome=str(input('digite seu nome completo:')).strip()
print('analisando seu nome...')
nome_maiusculo=nome.upper()
print('seu nome em maiúsculas é {}'.format(nome_maiusculo))
nome_minusculo=nome.lower()
print('seu nome em minúsculas é {}'.format(nome_minusculo))

#Remover espaços em branco e contar apenas as letras

nome_sem_espaços = nome.replace(" ", "")          #Aqui você está substituindo os espaços em branco
total_letras=len(nome_sem_espaços)                   #Aqui você está contando o comprimento do nome sem espaços
print('seu nome tem ao todo {} letras'.format(total_letras))

primeiro_nome=nome.split()[0]
print('seu primeiro nome é {} e ele tem {}'.format(primeiro_nome, len(primeiro_nome)))












