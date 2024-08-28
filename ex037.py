# Solicitar ao usuário um número inteiro
número_inteiro = int(input('\033[1;36mDigite um número inteiro:\033[m'))

# Exibir as opções de conversão
print('escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

# Solicitar ao usuário a escolha da base de conversão
opção = int(input('Sua opção:'))

# Converter para binário
numero_binário = bin(número_inteiro)[2:]  # Remover os dois primeiros caracteres (prefixo '0b')

# Converter para octal
numero_octal = oct(número_inteiro)[2:]  # Remover os dois primeiros caracteres (prefixo '0o')

# Converter para hexadecimal
numero_hexadecimal = hex(número_inteiro)[2:]  # Remover os dois primeiros caracteres (prefixo '0x')

if opção == 1:
    print(f'{numero_binário}')
elif opção == 2:
    print(f'{numero_octal}')
elif opção == 3:
    print(f'{numero_hexadecimal}')
else:
    print('Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).')
    




