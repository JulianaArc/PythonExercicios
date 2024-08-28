ficha_aluno = []
while True:
    nome = input('Nome: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha_aluno.append([nome, [nota_1, nota_2], media])
    c = input('Quer continuar? [S/N] ').upper()
    if c == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha_aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interromper): '))
    if opc == 999:
        break
    if opc <= len(ficha_aluno) - 1:
        print(f'Notas de {ficha_aluno[opc][0]} são {ficha_aluno[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
