preco = float(input('Qual o preço do produto ?'))
desconto = preco*5/100
total = preco-desconto
print('O produto custava R${:.2f},'
      ' na promoção com desconto de 5%, ele custará R${:.2f}'
       .format(preco, total))