salario = float(input('Digite o salario do funcionário:'))
if salario <= 1250.00:
    print('O novo salario terá acréscimo de 15%, sendo o total de R${}'
          .format(salario+(15*salario/100)))
else:
    print('O novo salario terá acréscimo de 10%, sendo o total de R${}'
          .format(salario+(10*salario/100)))