def exibir_mensagem():
    print("Olá, Mundo")

resposta = "sim"

while resposta == "sim":
    exibir_mensagem()
    resposta = input("Deseja exibir novamente? (sim/não): ").lower()

    while resposta != "sim" and resposta != "não":
        print("Erro: digite apenas sim ou não.")
        resposta = input("Deseja exibir novamente? (sim/não): ").lower()

print("Fim")