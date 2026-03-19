print ("ola mundo")

print (7+4)
print ("7" + "4")
print ("7+4") # CONCATENANDO STRINGS

# Comentário de 1 linha
'''
 Comentarios de 
 multiplas 
 linhas
'''
# Variaveis
nome = "Lucas" # str
print(nome)
idade = "18" # int
peso = "70.2" # float

print ("oiii \n", nome, idade, peso)
print (f"Olá, {nome}!!!")

# Input -- simulação de um forms no cmd
nome = input("Digite o seu nome: ")
idade = int(input ("Digite sua idade: "))
peso = input ("Digite seu peso: ")

print(nome, idade, peso)
print (idade + 1)

anoNascimento = 2008
anoAtual = 2026

idade = anoAtual - anoNascimento
print (f"Sua idade é: {idade}")