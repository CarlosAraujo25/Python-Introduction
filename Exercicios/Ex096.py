def area(a, b):
    area = a * b
    print(f'A área de um terreno {a}x{b} é de {area}m²')


print('Controle de Terreno')
print('-' * 25)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
print(area(a, b))