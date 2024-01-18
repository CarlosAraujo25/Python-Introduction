from random import randint
cont = 0
print('-=-'*30)
print('VAMOS JOGAR UM JOGO.')
print('-=-'*30)
while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0, 10)
    soma = jogador + computador
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar?[P/I]')).strip().upper()[0]
    print(f'''Você jogou {jogador} e o computador {computador}, o total é de {jogador + computador}''')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    soma = jogador + computador
    if soma % 2 == 0 and pi == 'P':
        print('Jogador venceu')
        cont += 1
    elif soma % 2 != 0 and pi == 'I':
        print('Jogador venceu.')
        cont += 1
    else:
        print('Computador Venceu.')
        break
    print('Vamos jogar novamente!')
print(f'GAME OVER. Você venceu {cont} vezes')
