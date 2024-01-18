from random import randint
computador = randint(0, 10)

print('Olá, sou seu computador... \n Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palplite?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns'.format(palpite))
