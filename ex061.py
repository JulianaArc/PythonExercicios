print("gerador de PA")
print("=-=" * 10)
p1 = int(input("primeiro termo:"))
r = int(input("razão:"))
c = 10
pa = p1
while c > 0:
    print(f"{pa} > ", end=" ")
    pa = pa + r
    c = c - 1
print("FIM")