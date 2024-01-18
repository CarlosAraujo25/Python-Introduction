aluno = {}
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['Situação'] = str('AProvado')
elif  5<= aluno['media'] < 7:
    aluno['Situação'] = str('Recuperação')
else:
    aluno['Situação'] = str('Reprovado')
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual {v}')
print()
