import math
'''catop = float(input('digite o comprimento do cateto oposto: '))
catadj = float(input('digite o comprimento do cateto adjascente: '))
hipotenusa = (catop**2 + catadj**2) ** (1/2)
print ('O valor do cateto da hipotenusa é {:.2f}'.format(hipotenusa))'''

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))