sexo = input('Informe seu sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':     # enquanto sexo for diferente de M e F
    sexo = input('Dados Inválidos. Por favor, informe seu sexo: ').upper()
if sexo == 'M':
    print('sexo M registrado com sucesso!')
else:
    print('Sexo F registrado com sucesso!')


#OU

sexo = input('informe seu sexo: [M/F]').strip().upper()[0] # elimina espaços, torna maiúscula, fatiamento(considera apenas a 1 letra digitada)
while sexo not in 'MmFf':  #enquanto sexo não estiver em feminino ou mascúlino
    sexo = input('Dados inválidos. Por favor, informe o seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')





