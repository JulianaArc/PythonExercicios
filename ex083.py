expressao = input('Digite sua expressão: ')

pilha = []  # Inicializa uma pilha vazia

# Percorre cada caractere na expressão
for c in expressao:
    if c == '(':  # Se encontrar um parêntese de abertura
        pilha.append(c)  # Adiciona à pilha
    elif c == ')':  # Se encontrar um parêntese de fechamento
        if pilha:  # Se a pilha não estiver vazia, ou seja, se tiver um '(' parêntese de abertura
            pilha.pop()  # Remove o último parêntese de abertura da pilha
        else:  # Se a pilha estiver vazia    #ou seja, considere como se a expressão digitada foi algo como: a + b), a pilha está fazia porque não foi digitado o '(', logo essa expressão é inválida.
            print('Expressão INVÁLIDA...')
            break
else:
    if pilha:  # Se a pilha ainda tiver elementos após o loop   #ou seja se mesmo após o loop onde o ')' apaga o '(' ficando assim fazia, tiver qualquer um desses elementos, significa que existem elementos a mais.
        print('Expressão INVÁLIDA...')
    else:
        print('Expressão VÁLIDA...')


# considere a expressão (a+b)

# Para entender você deve DESCONSIDERAR totalmente o que está dentro dos parênteses
# considere que existe apenas ()
# até porque são apenas eles que vão para dentro da lista pilha
# com base nisso, a teoria diz que quando o loop encontra um '(' parentese de abertura ele adiciona a lista pilha
# ou seja, o '(' fica armazenado dentro da lista pilha ['(']
# em seguida são lidos os números e os sinais: (a+b, mas entenda bem, são APENAS LIDOS, não são armazenados.
# Logo, a pilha continua sendo apenas ['('].
# Mas algo muda quando o programa encontra o ')' parêntese de fechamento.
# Quando isso finalmente acontece vericamos se temos o ['('] parêntese de abertura na pilha, e nesse exemplo, nós temos.
# E quando isso acontece ao invés de adicionar também o ')' parêntese de fechamento na pilha, para ficar [()].
# Isso não acontece. Quando o programa ler o ')' parêntese de fechamento e encontra dentro da lista o ')' parêntese de abertura
# O programa entende que '(' encontrou seu par ')', e então remove o '(' parêntese de abertura da pilha
# Deixando assim ela zerada: [].
# MAS POR QUE ISSO ACONTECE?
# A lógica é que cada '(' deve ter um correspondente ')'. Quando encontramos '(', esperamos que eventualmente encontraremos ')'.
# Quando encontramos ')', verificamos se temos um '(' correspondente na pilha:
# Remover '(' ao encontrar ')': indica que o ')' fechou o último '('. E assim a pilha zera.


#Expressão: (a+b) ilustrado

#Pilha: []
#Ler '('
# A pilha recebe o '('
#Pilha agora é: ['(']

#Ler a:
#a é ignorado quanto à pilha.
#Pilha continua sendo: ['(']

#Ler +:
#+ é ignorado quanto à pilha.
#Pilha continua sendo: ['(']

#Ler b:
#b é ignorado quanto à pilha.
#Pilha continua sendo: ['(']

#Ler ')':
#Verificamos a pilha: contém ['(']
#Removemos '(' da pilha.
#Pilha: []





