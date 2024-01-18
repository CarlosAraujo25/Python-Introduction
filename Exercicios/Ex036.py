from time import sleep
print('Olá, vamos verificar algumas informações pessoais \n'
      ' para verificar a possibilidade de financiamento.')

casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual o valor do seu salario? R$'))
anos = int(input('Em quantos anos você deseja financiar ?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('PROCESSANDO...')
sleep(3)
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('PARABÉNS! Seu financiamento foi aprovado.')
else:
    print('Infelizmente sua tentativa de financiamento foi negada.')
