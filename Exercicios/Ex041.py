from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9:
    print('Este atleta tem {} anos, '
          'ele é um atleta mirim.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Este atleta tem {} anos, '
          'ele é um atleta infatil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Este atleta tem {} anos,'
          ' ele é um atleta junior.'.format(idade))
elif idade <= 25:
    print('Este atleta tem {} anos,'
          ' ele é um atleta sênior.'.format(idade))
elif idade > 25:
    print('Este atleta tem {} anos,'
          ' ele é um atleta master.'.format(idade))