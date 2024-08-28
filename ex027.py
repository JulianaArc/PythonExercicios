nome=str(input('digite seu nome completo:')).strip()
print('muito prazer em te conhecer!')
print('seu primeiro nome é {}'.format(nome.split()[0]))
print('seu último nome é {}'.format(nome.split()[-1]))

# Quando você usa [0] após split(), você está acessando o primeiro elemento da lista resultante da divisão da string.
# Da mesma forma, quando você usa [-1] após split(), você está acessando o último elemento dessa lista.
# Da mesma forma, -2 acessaria o penúltimo elemento, -3 acessaria o antepenúltimo e assim por diante.


