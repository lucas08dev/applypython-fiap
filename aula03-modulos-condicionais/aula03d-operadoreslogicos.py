# logica and

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no programa")

# logica or

logica_or = False or False or True
print(logica_or)

# logica not
negacao = not False
print (negacao)

if not login:
    print("Login errado, amigo.")


