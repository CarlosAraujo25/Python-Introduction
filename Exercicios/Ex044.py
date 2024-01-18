print('{:=^40}'.format(' LOJAS ARAÚJO '))

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input("Qual é a opção ? "))


if opcao == 1:
    print('Sua compra será paga à vista no dinheiro, tendo 10% de desconto'
          ' \n no valor de R${:.2f}, sendo o total a pagar de R${:.2f}.'
          .format(preco * 10 / 100, preco - preco * 10 / 100))
elif opcao == 2:
    print('Sua compra será paga no cartão, tendo 5% de desconto'
          ' \n no valor de R${:.2f}, sendo o total a pagar de R${:.2f}'
          .format(preco * 5 / 100, preco - preco * 5 / 100))
elif opcao == 3:
    print('Sua compra será parcelada em 2x e não terá desconto, \n'
          ' o valor a ser pago é de R${:.2f}'.format(preco))
elif opcao == 4:
    parcela = int(input('Qual a quantidade de parcelas desejadas ? '))
    juros = (preco * 20 / 100)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS. \n'
          'Sua compra de R${:.2f} vai custar R${:.2f} no final.'
          .format(parcela, (juros + preco) / parcela, preco, preco + juros))
else:
    print('\033[31mOpção inválida de pagamento. Tente novamente.\033[m')