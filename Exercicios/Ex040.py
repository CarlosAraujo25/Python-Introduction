n1 = float(input('digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2

if media  < 5.0:
    print('A nota deste aluno foi {}, ele está Reprovado'.format(media))
elif media <= 6.9 and media >= 5.0:
    print('A nota deste aluno foi {}, ele está de Recuperação'.format(media))
else:
    print('A nota deste aluno foi {}, ele está aprovado'.format(media))

