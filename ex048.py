soma = 0  # Inicializa a variável soma
count = 0 # Inicializa a variável count (um contador) para contar o número de valores que atendem aos critérios.
# Loop através de todos os números de 1 a 500
for num in range(1, 501):
    # Verifica se o número é ímpar e múltiplo de 3
    if num % 2 == 1 and num % 3 == 0:
        soma += num  # Adiciona o número à soma
        count = count + 1 #adiciona 1 cada vez que um número atender aos critérios.
# Imprime o resultado
print(f"A soma de todos os {count} valores solicitados é {soma}")


# EXPLICAÇÃO DETALHADA
# 1. soma = 0: Neste momento, você está criando uma variável chamada soma e atribuindo o valor inicial de 0 a ela.
# Isso é como criar uma caixa vazia e rotulá-la como "soma".

# 2. for num in range(1, 501):: Aqui, você está dizendo ao Python para percorrer todos os números de 1 a 500 (o número 501 não está incluído).
# A cada iteração, o número atual é armazenado na variável num.

# 3. if num % 2 == 1 and num % 3 == 0:: Dentro do loop, você está testando se o número atual (num) é ímpar e se é divisível por 3.
# Se ambos os critérios forem atendidos, isso significa que o número é ímpar e múltiplo de 3.

# 4. soma += num: Se o número atender aos critérios, ele é adicionado à variável soma.
# Essa expressão soma += num é uma forma compacta de escrever soma = soma + num,
# que significa "adicione o valor atual de num ao valor atual de soma e armazene o resultado de volta em soma".
# Isso é como colocar o valor de num dentro da caixa rotulada como "soma".


# MAIS EXPLICAÇÃO
# o soma=0 é como se fosse uma caixinha, nesse momento ela não tem nenhum número dentro, mas depois de:
# for num in range(1, 501):
# if num % 2 == 1 and num % 3 == 0:
# é como seu eu estivesse dizendo especificamente o que colocar dentro dessa caixinha e faço isso usando a soma ''soma = soma + num''

