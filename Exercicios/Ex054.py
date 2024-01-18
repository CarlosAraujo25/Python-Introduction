from datetime import date
atual = date.today().year
menor = 0
maior = 0
for pes in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(pes)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idadde.'.format(menor))
