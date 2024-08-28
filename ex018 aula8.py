import math
ângulo=float(input('digite o ângulo que voçê deseja:'))
seno=math.sin(math.radians(ângulo))
print('o ângulo de {:.2f} tem seno de {:.2f}'.format(ângulo,seno))
cosseno=math.cos(math.radians(ângulo))
print('o ângulo de {:.2f} tem cosseno de {:.2f}'.format(ângulo,cosseno))
tangente=math.tan(math.radians(ângulo))
print('o ângulo de {:.2f} tem tangente de {:.2f}'.format(ângulo,tangente))


