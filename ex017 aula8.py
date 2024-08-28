from math import sqrt
C1=float(input('comprimento do cateto oposto:'))
C2=float(input('comprimento do cateto adjacente:'))
hipotenusa=sqrt(C1**2 + C2**2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
