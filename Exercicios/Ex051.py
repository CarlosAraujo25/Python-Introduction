print('='*20)
print('10 TERMOS DE UMA P.A.')
print('='*20)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo1 + (10 - 1) * razao
for c in range(termo1, decimo + razao, razao):
    print('{}'.format(c), end=' => ')
print('ACABOU')