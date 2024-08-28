número = 0
quantidade = 0
soma = 0

while número != 999:
    número = int(input('Digite um número [999 para parar]: '))
    if número != 999:
        quantidade += 1
        soma += número

print(f'Você digitou {quantidade} números e a soma entre eles foi {soma}')
