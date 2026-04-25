import math

# Calcule a raiz de um número usando a função sqrt do módulo math. O número deve ser fornecido pelo usuário.

import math


numero = float(input("Digite um número para calcular a raiz quadrada: "))
raizquadrada = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raizquadrada:.2f}")

# Verifique se um número é par ou ímpar usando o operador módulo (%). O número deve ser fornecido pelo usuário.
numero = int(input("Digite um número para verificar se é par ou ímpar: "))
if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")

# Calcule a potência de um número usando o operador de exponenciação (**). O número base e o expoente devem ser fornecidos pelo usuário.
base = float(input("Digite a base para calcular a potência: "))
expoente = float(input("Digite o expoente para calcular a potência: "))
potencia = base ** expoente
print(f"{base} elevado a {expoente} é igual a {potencia:.2f}")