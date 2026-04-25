# escolha do usuario
# 0 --> sair
# 1 --> entrar
# ----> erro!

escolha_usuario = int(input("Digite o que deseja fazer: "))

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro!")