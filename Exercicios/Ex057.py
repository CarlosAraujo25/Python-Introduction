print('Para encerrar o programa, digite 0.')
sex = input('Informe seu sexo: [M/F]').upper().strip()[0]
while sex not in 'MmFf':
    sex = str(input('Dados invalidos, por favor, informe seu sexo.')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sex))
