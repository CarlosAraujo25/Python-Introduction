from time import sleep

print('Vamos descobrir se seus segmentos de retas podem formar um triângulo')

r1 = float(input('Digite o valor de um segmento de reta: '))
r2 = float(input('Digite o valor de outro segmento de reta: '))
r3 = float(input('Digite o valor de um terceiro segmento de reta: '))
print('\033[:33mPROCESSANDO...\033[m')
sleep(3)
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('\033[0:32mPARABÉNS! Seus segmentos de reta podem formar um triângulo.\033[m')

    if r1 == r2 == r3:
        print('Seus segmentos de retas formam um \033[0:32mTriângulo Equilátero.\033[m \n'
              'Possuindo todos os lados iguais.')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Seus segmentos de retas formam um \033[:32mTriângulo Isósceles.\033[m \n'
              'Possuindo dois lados iguais.')
    elif r1 != r2 != r3 != r1:
        print('Seus segmentos podem formar um \033[:32mTriângulo Escaleno.\033[m \n'
              'Possuindo todos os lados diferentes.')

else:
    print('\33[:31mSeus segmentos de reta NÃO podem formar um triângulo\033[m')
