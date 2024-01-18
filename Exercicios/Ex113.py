def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um valor inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar esse valor.\033[m')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real:')
print(f'O valor inteiro digitado foi {inteiro} e o valor real foi {real}')
