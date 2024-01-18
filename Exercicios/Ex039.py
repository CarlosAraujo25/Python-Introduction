from datetime import date
data = int(input('digite o ano do seu nascimento:'))
atual = date.today().year
idade =  atual - data
alistamento = 18 - idade
if idade < 18:
    print('Você só tem {} anos, ainda não chegou a'
          ' hora de você se alistar, faltam {} anos.'
          .format(idade, alistamento))
elif idade == 18:
    print('Você já tem {} anos, apresentesse '
          'a junta de alistamento militar da sua cidade.'
          .format(idade))
else:
    print('Você possui {} anos, você deveria ter se alistado há {} anos,\n'
          ' pague a multa por atraso e apresentesse \n '
          'a junta de alistamento militar da sua cidade.'
          .format(idade, idade - 18))