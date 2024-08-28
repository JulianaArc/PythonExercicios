primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
números = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(números)))
print('O menor numero digitado foi {}'.format(min(números)))


#ou
a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
c = int(input('terceiro valor:'))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor é {}'.format(menor))
print('o maior valor é {}'.format(maior))

