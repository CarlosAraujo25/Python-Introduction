soma = quant = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um numero:'))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('você digitou {} numeros e a media foi de {}'.format(quant, media))
print('O menor valor foi {} e o maior foi {}'.format(menor, maior))
