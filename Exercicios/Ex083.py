expr = str(input('Digite uma expressão matematica: '))
pilha = []
for letra in expr:
    if letra == '(':
        pilha.append('(')
    elif letra == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão é válida.')
else:
    print('A sua expressão não é válida.')
