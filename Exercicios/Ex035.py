print('\033[0:33m-=-\033[m' * 20)
print('Analisador de Triângulos.')
print('\033[:33m-=-\033[m' * 20)

r1 = float(input('Digite o valor de um segmento de reta:'))
r2 = float(input('Digite o valor de um outro segmento de reta: '))
r3 = float(input('Digite o valor de um terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes segmentos podem formar um triângulo.')
else:
    print("Este segmentos NÃO podem formar um triângulo.")
