km = float(input('Qual a distância da sua viagem em km? '))
if km <= 200:
    print('O preço cobrado será de R${:.2f}'.format(km*0.5))
else:
    print('A viagem excede os 200km. O preço cobrado será de R${:.2f}'.format(km*0.45))
