aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))
print('-='*30)
aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'recuperação' if 5 <= aluno['média'] <7 else 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')


