# TUPLAS
print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche)

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3])

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3])

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:])  #do elemento 2 até o final

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])  #do início até o elemento 2

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2:])

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3:])

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi bastante!')

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))

print('='*20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
for count in range(0, len(lanche)):
    print(count)

print('=' * 20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
for count in range(0, len(lanche)):
    print(lanche[count])

print('=' * 20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
for count in range(0, len(lanche)):
    print(f'eu vou comer {lanche[count]} na posição {count}')

print('=' * 20)


lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')

print('=' * 20)

lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))   #coloca em ordem alfabetica

print('='*20)


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)  # não vai somar, vai apenas juntar

print('='*20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(len(c))   #vai mostar quantos elementos tem (nesse caso 7)

print('='*20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))  #vai mostar quantas vezes aparece o número 5 (nesse caso 2)

print('='*20)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(4)) # vai mostar em qual posição está o 4 (nesse caso está na 6), (#lembre-se que a contagem começa em 0)







