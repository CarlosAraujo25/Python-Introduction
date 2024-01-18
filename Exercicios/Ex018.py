from math import sin, cos, tan, radians
an = float(input("Digite um angulo: "))
sen = sin(radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, sen))
cos = cos(radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tan))