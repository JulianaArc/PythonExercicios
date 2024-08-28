for count in range(2, 51, 2):   #contagem de números pares do 1 até o 50
    print(count, end=' ')
print('ACABOU')


# OU
for count in range(1, 51):
    if count % 2 == 0:    #se o número é divisível por 2, ele é par.
        print(count, end=' ')
print('acabou')

