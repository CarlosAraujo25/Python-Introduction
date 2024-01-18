n1 = float(input('Digite um valor em metros:'))
n2 = n1*100
n3 = n1*1000

print('O valor digitado é de {}m.'
      ' que corresponde a {:.0f}cm e {:.0f}mm'
      .format(n1, n2, n3))