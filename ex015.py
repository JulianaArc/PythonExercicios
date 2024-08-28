d=int(input('quantos dias alugados?'))
km=float(input('quantos km rodados?'))
T=(d*60)+(km*0.15)
print('o total a pagar é de R${:.2f}'.format(T))
