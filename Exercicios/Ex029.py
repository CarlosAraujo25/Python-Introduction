km = float(input('Qual a velocidade em km/h do carro:'))
multa = (km - 80) * 7
if km >= 80:
    print('Você foi multado. A multa vai lhe custar R${:.2f}'.format(multa))
