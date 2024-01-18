num = int(input('Digite um numero para ver sau tabuada: '))
print('-'*12)
for t in range(0, 11):
    print('{} x {} = {}'.format(num, t, t*num))
print('-'*12)