print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
while True:
    idade = int(input('Idade:'))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Sexo: [M/F]')).strip().upper()[0]
    maior18 = m = f = 0
    if idade >= 18:
        maior18 += 1
    if genero == 'M':
        m += 1
    if idade < 18 and genero == 'F':
        f += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if n == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {m} homens cadastrados')
print(f'E temos {f} mulher com menos de 20 anos.')
