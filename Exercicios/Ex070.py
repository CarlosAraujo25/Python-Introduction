print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
menor = cont = total = totmil = 0
menorstr = ' '
while True:
    nome = str(input('Nome do Produto:')).strip().upper()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        menorstr = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorstr} custando R${menor}')
