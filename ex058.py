import random
tentativas_palpite = 0

print('Sou seu computador...')
print('acabei de pensar em um número entre 0 e 10.')
print('será que você consegue adivinhar qual foi?')

palpite = int(input('Qual é seu palpite? '))
número_pensado = random.randint(0, 10)

while palpite != número_pensado:  #enquanto palpite for diferente do número pensado
    if palpite < número_pensado: # se palpite for menor que o número pensado
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    palpite = int(input('qual é seu palpite? '))
    tentativas_palpite += 1  # ou tentativas_palpite = tentativas_palpite + 1, # Incrementa o contador de tentativas após cada palpite incorreto

tentativas_palpite += 1  # Incrementa o contador de tentativas após o palpite correto
print(f'Acertou com {tentativas_palpite} tentativas, parabéns!')


# NOTAS
# Eu poderia ter usado um if após o loop while, ficaria algo como:
# if palpite == número pensado
#    print(f'Acertou com {tentativas_palpite} tentativas, parabéns!')
# no caso em questão, pode-se evitar o uso de um bloco if após o loop while.
# O loop while será executado até que o palpite do usuário seja igual ao número pensado, então,
# se o código chegar à linha de impressão "Acertou com {} tentativas, parabéns!", isso significa que o palpite do usuário é igual ao número pensado.
# Portanto, não há necessidade de verificar novamente com um if.

# O MOTIVO DE EXISTIR a linha 19 após o loop while: tentativas_palpite += 1  # Incrementa o contador de tentativas após o palpite correto
# anteriormente, sem a existência da mesma, o contador contava apenas os palpites incorretos, deixando de lado o último número (o número adivinhado).
# Agora, Isso garantirá que o número de tentativas contabilizadas seja correto, garantindo assim que o número que for acertado tbm esteja dentro da contagem.

