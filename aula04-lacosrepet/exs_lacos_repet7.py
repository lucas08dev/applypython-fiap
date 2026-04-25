n = int(input("Digite um valor: "))

while n <=0:
    print("Valor inválido!")
    n = int(input("Digite novamente o valor: "))

soma = 0

for i in range(1, n + 1):
    soma += i

print(f"O resultado é: {soma}")