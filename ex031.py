distância=float(input('qual a distância da sua viagem?:'))
print('você está prestes a começar uma viagem de {}km'.format(distância))
if distância<=200:   #se a distãncia for menor ou igual a 200
    preço_da_passagem = distância * 0.50
else:
    preço_da_passagem = distância * 0.45

print('o preço da passagem é de R${:.2f}'.format(preço_da_passagem))


#ou
preço = distância * 0.50 if distância <= 200 else distância * 0.45






