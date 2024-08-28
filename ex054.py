import datetime
ano_atual = datetime.datetime.now().year
maiores = 0
menores = 0

for c in range(1, 8):
    ano = (int(input(f'Em que ano a {c}ª pessoa nasceu: ')))
    if ano_atual - ano >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade')






