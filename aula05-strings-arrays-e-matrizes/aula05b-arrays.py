lista_de_frutas = ["Banana", "Maçã", "Morango"]

#lista_de_frutas[0] = "Banana"
#lista_de_frutas[1] = "Maçã"
#lista_de_frutas[2] = "Morango"

print(lista_de_frutas[0])

lista_de_frutas.append("Pera")
print(lista_de_frutas)

qtd_frutas = len(lista_de_frutas)
print("Qtd de frutas: ", qtd_frutas)

# for indexado para percorrer
for i in range(qtd_frutas):
    print(lista_de_frutas[i])

print()

# for each em Python

for fruta in lista_de_frutas:
    print(fruta)

numeros = [0, 5, 11, 4]
for numero in numeros:
    print(numero)


