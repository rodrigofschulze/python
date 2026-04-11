usuario = input( "Digite um usuario")
senha = input( "Digite uma senha")
if usuario == "admin":
    if senha == "1234":
        print("Login feito com sucesso")
    else:
        print("Falha no login")
else:
    print("Falha no login")