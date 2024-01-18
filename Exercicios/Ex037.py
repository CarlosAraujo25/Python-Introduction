num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção:  '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual há {}.'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual há {}.'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual há {}.'.format(num, hex(num)))
else:
    print('OPção inválida.')