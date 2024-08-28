a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('os segmentos acima PODEM FORMA triângulo', end=' ')
    if a == b and a == c and b == c:
        print('EQUILÁTERO!')
    elif a != b and a != c and b != c:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
