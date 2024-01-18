n = cont = soma = 0
while True:
    n = int(input('digite um numero: [999 para parar.}'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} numeros e a soma deles é de {soma}.')
