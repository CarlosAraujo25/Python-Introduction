#Usando While para contar 10 numeros.
n = c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        print('Programa Encerrado com Sucesso!')
        break
    print('-'*30)
    while c <= 9:
        c += 1
        print(f'{n} x {c} = {n * c}')
    c = 0
    print('-'*30)

###########################################################
#Usando For para contar 10 numeros.

c = 0
while True:
    n = int(input('Quer ver a tabuada de qual numeero?'))
    if n < 0:
        print('Programa Encerrado com sucesso!')
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-'*30)
