def exibir_mensagem():
    print("Hello World")

resposta = "sim"

while resposta == "sim":
    exibir_mensagem()
    resposta = input("Deseja exibir a mensagem novamente? ").lower()

print("FIM")


def repetir():
    n = int(input("Digite um número inteiro: "))
    numero = n * 2
    print(f"O dobro é: {numero}")

resp = "sim"

while resp == "sim":
    repetir()
    resp = input("Você deseja continuar? ").lower()

print("Programa encerrado")


def mensagem():
    print("Bem-vindo ao sistema!")

res = "sim"

while res == "sim":
    mensagem()
    res = input("Deseja exibir a mensagem novamente? ").lower()

print("Até logo!")


def mostrar_mensagem():
    print("Sistema de notas iniciado!")

respos = "sim"

while respos == "sim":
    mostrar_mensagem()
    respos = input("Deseja ver a mensagem novamente? ").lower()

print('Sistema finalizado.')


def quadrado_numero():
    numero = int(input("Digite um número: "))
    quadrado = numero * numero
    print(f"O quadrado deste número é: {quadrado}")

resp = "sim"
contador = 0

while resp == "sim":
    quadrado_numero()
    contador += 1
    resp = input("Deseja continuar? ").lower()

print(f"Você executou o programa {contador} vezes")
print("Programa encerrado.")