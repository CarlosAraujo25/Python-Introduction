from turtle import Turtle

t = Turtle()
t.speed(1)
resp = ' '
while True:
    frente_tras = ''
    direita_esquerda = ''
    while True:
        frente_tras = str(input('Deseja movimentar para frente ou para trás? [F/T]')).strip().upper()[0]
        if frente_tras in 'TF':
            break

    if frente_tras == 'F':
        frente = int(input('Quantos pixels a frente devem ser percorridos? '))
        t.forward(frente)
    else:
        tras = int(input('Quantos pixels para trás devem ser percorridos? '))
        t.backward(tras)

    while True:
        direita_esquerda = str(input('Qual angulo deseja rotacionar? [E/D]')).strip().upper()[0]
        if direita_esquerda in 'ED':    
            if direita_esquerda == 'D':
                direita = int(input('Qual angulo a tartaruga deve girar para a direita? '))
                t.right(direita)
                break
            if direita_esquerda == 'E':
                esquerda = int(input('Qual angulo a tartaruga deve girar para a esquerda?'))
                t.left(esquerda)
                break
    
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp not in 'SN':
        print('ERRO! Por favor, digite uma resposta válida.')
    elif resp == 'N':
        print('PROGRAMA FINALIZADO¹')
        break