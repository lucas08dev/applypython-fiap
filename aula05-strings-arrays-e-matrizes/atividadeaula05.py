nomes = ["João", "José", "Enzo", "Ana"]
lista_nomes = len(nomes)

for i in range(lista_nomes):
    for j in range(i+1,lista_nomes):
        print(nomes[i], nomes[j])