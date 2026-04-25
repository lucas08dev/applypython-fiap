def validar_nota(nota):
    nota_temp = nota
    while nota_temp < 0 or nota_temp > 10:
        print("Erro: A nota deve estar entre 0 e 10!")
        nota_temp = float(input("Digite novamente a nota: "))
    return nota_temp

nota_1 = float(input("Digite a primeira nota: "))
nota_1 = validar_nota(nota_1)

nota_2 = float(input("Digite a segunda nota: "))
while nota_2 < 0 or nota_2 > 10:
    print("Erro: A nota deve estar entre 0 e 10!")
    nota_2 = float(input("Digite novamente a segunda nota: "))

media = (nota_1 + nota_2) / 2

print(f"A média final é: {media}")