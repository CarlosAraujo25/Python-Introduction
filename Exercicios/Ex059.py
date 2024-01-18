from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('digite outro valor: '))
opcao = 0
while opcao != 5:
        print('''
O que deseja realizar com esses valores ?
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] sair do programa
        ''')
        opcao = int(input('Qual sua opção ?'))
        if opcao == 1:
                soma = n1 + n2
                print('A soma entre {} + {} é de {}.'.format(n1, n2, soma))
        elif opcao == 2:
                mult = n1 * n2
                print('A múltiplicação entre {} x {} é de {}'.format(n1, n2, mult))
        elif opcao == 3:
                maior = n1
                if n2 > n1:
                        maior = n2
                print('O maior numero é {}'.format(maior))
        elif opcao == 4:
                print('Informe os números novamente:')
                n1 = int(input('Digite um valor: '))
                n2 = int(input('Digite outro valor: '))
        elif opcao == 5:
                print('Finalizando programa.')
        else:
                print('Opção inválida.')
        sleep(2)
print('Fim do programa. Volte sempre.')
