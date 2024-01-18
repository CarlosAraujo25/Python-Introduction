n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite um terceiro mumero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi {}.'.format(menor))
maior = n3
if n2 > n3 and n2 > n1:
    maior = n2
if n1 > n3 and n1 > n2:
    maior = n1
print('O maior valor digitado foi {}.'.format(maior))