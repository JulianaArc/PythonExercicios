#Condições

nome=str(input('qual é o seu nome?'))
if nome=='Gustavo':
    print('que nome lindo voê tem!')
else:
    print('seu nome é tão normal!')
    print('Bom dia, {}!'.format(nome))



#outro exemplo de Condiçoes:

n1=float(input('digite a primeira nota:'))
n2=float(input('digite a segunda nota:'))
m=(n1+n2)/2
print('a sua média foi {:.1f}'.format(m))
if m>=6.0:
    print('sua média foi boa! PARABÉNS!)')
else:
    print('sua média foi ruim! ESTUDE MAIS!')


#ou

n1=float(input('digite a primeira nota:'))
n2=float(input('digite a segunda nota:'))
m=(n1+n2)/2
print('a sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m>=6 else 'ESTUDE MAIS!')
