num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo um numero: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareeceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')
