# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem PARES.
# Se o valor digitado for ímpar, desconsidere-o.

soma=0
for c in range(1,7):
    num=int(input('digite um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
print(f'a soma dos números pares informados é {soma}')


