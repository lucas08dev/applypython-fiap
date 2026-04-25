for cp in range(3):
    print(f"Produto {cp}")

for i in range(0, 12, 2):
    print(i)

qtd = int(input("Digite a qtd de produtos: "))

for i in range (qtd):
    print(f"Produto {i+1}")

# Laço encadeado

for i in range(0, 5):
    for j in range (0, 4, 2):
        print(f"i: {i}, j: {j}")


for c in range(1, 7):
    print(c)

for a in range(7, 1, -1):
    print(a)


n = int(input("Digite um número: "))
print(f"Contagem de 1 até {n}: ")
for c in range(1, n+1):
    print(c)


i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for i in range(i, f+1, p):
    print(i)


s = 0
for i in range(4):
    n = int(input("Digite um valor: "))
    s += n

print(s)
print("fim")
