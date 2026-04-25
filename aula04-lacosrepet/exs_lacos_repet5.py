for i in range(5):
    n = int(input("Digite um valor: "))
    
    if i == 0:
        valor = n
    elif n > valor:
        valor = n

print(f"O maior valor é: {valor}")