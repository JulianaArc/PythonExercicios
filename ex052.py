n = int(input('Digite um número: '))
total = 0  # Inicializa a variável para contar o número de divisores
divisores = []   # Lista para armazenar os divisores do número digitado
# Loop de 1 a n para verificar os divisores do número digitado
for c in range(1, n + 1):
    # Verifica se o número digitado é divisível por c
    if n % c == 0:
        # Se for divisível, incrementa o total de divisões
        total += 1
        # Adiciona o divisor à lista de divisores
        divisores.append(c)  # Armazena os números divisores de n
        # Imprime o divisor em amarelo, pois é um divisor de n
        print(f'\033[33m{c}\033[m', end=' ')
    else:
        # Imprime o resto em branco, pois não é um divisor de n
        print(f'\033[97m{c}\033[m', end=' ')

# Verifica se o número é primo com base na quantidade de divisores
if total == 2:
    # Se tiver exatamente 2 divisores, o número é primo
    print(f'\nO número {n} foi divisível {total} vezes, por isso ele É PRIMO!')
else:
    # Se tiver mais ou menos de 2 divisores, o número não é primo
    print(f'\nO número {n} foi divisível {total} vezes, por isso ele NÃO É PRIMO!')
