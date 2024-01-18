times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São paulo', 'Fluminense', 'Sport Recife', 'EC Vitoria', 'Curitiba', 'Avaí',
         'Ponte Preta', 'Atlético-GO')
print('-='*30)
print(f'Lista de times: {times}')
print('-='*30)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')