altura = float(input('Digite a sua altura em metros:'))
peso = float(input('Digite o seu peso em kg: '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Você tem o IMC de {:.2f}, você está abaixo do peso.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Você tem o IMC de {:.2f}, você está com o peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Você esta com IMC de {:.2f}, você está com sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Você está com IMC de {:.2f}, você está com obesidade.'.format(imc))
elif imc > 40:
    print('Você esta com o IMC de {:.2f}, você está com obesidade mórbida.'.format(imc))
