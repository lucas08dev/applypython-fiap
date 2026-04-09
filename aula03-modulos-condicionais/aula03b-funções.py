 # Função sem retorno sem parâmetro.

def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()
print_lyrics()


 # Função sem retorno com parâmetro.
def boas_vindas(nome):
    print(f"Olá, {nome}!! Seja bem vindo!")

nome_digitado = input("Digite o seu nome: ")
boas_vindas(nome_digitado)

# Função com retorno com parâmetro

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

print(soma(18, 16))
print(type(nome_digitado))
