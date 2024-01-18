s = float(input('O salário de funcionario é de:'))
a = s*15/100
total = s+a
print('O aumento no salário é de 15%, totalizando {:.2f}.'
      'Tendo um aumento de R${:.2f}.'
      .format(total, a))