import os

# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
frutas = ['maça', 'banana', 'ameixa', 'pêra', 'laranja']

cores = ['vermelho', 'azul', 'amarelo', 'verde', 'roxo']

linguagens = ['python', 'php', 'brainf***k', 'java', 'javascript']

with open('frutas.txt', 'w', encoding='utf-8', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
with open('frutas.txt', 'r', encoding='utf-8') as ler_arquivo:
    for linha in ler_arquivo:
        print(linha)

# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
with open('frutas.txt', 'a', encoding='utf-8') as add_cores:
    for cor in cores:
        add_cores.write(cor + os.linesep)

# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
with open('linguagens.txt', 'w', encoding='utf-8', newline='') as ling:
    for linguagem in linguagens:
        ling.write(linguagem + os.linesep)
# BONUS - Como você poderia criar vários arquivos vazios, usando um laço for?
arquivos = ['musicas.mp3', 'fotos.jpg', 'video.mp4', 'relatorios.pdf', 'orçamentos.xlsx']
for arquivo in arquivos:
    with open(arquivo, 'w') as arquivo:
        pass
