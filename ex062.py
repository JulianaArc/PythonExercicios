print("Gerador de PA")
print("=-=" * 10)

p1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
c = 10
pa = p1
mais = 10  # Inicializando a variável mais para permitir a entrada no loop
total = 0

while mais != 0:
    while c > 0:
        print(f"{pa} > ", end="")
        pa = pa + r
        c = c - 1
        total = total + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais (0 para sair): '))
    c = mais

print(f'progressão finalizada com {total} termos mostrados')