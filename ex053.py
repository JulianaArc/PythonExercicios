frase = (str(input('Digite uma frase: '))).strip().upper().replace(" ","")
print(f'O inverso de {frase} é {frase[::-1]}')
if frase == frase[::-1]:  #verifica se a frase original é igual à sua versão invertida.
    print('A frase digitada é palíndromo')
else:
    print('A frase NÃO É um palíndromo')


# NOTAS
# strip(): Remove espaços em branco no início e no final da string,
# garantindo que não haja espaços extras que possam interferir na análise.

# upper(): Este método transforma toda a string em maiúsculas.
# Isso é feito para garantir que a comparação de palíndromo não seja sensível a maiúsculas e minúsculas.

# replace(" ", ""): Este método substitui todos os espaços em branco (representados por " ") na string
# por uma string vazia "", ou seja, remove todos os espaços em branco da frase.

