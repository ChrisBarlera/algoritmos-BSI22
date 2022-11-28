print('/////Cadastre-se://///')
login = input("Login: ")
senha = input("Senha: ")

print('\n/////Faça o acesso://///')
tentativaLogin = input("Login: ")
tentativaSenha = input("Senha: ")

if tentativaLogin == login:
    if tentativaSenha == senha:
        print('Acesso concedido!')
    else:
        print('Senha incorreta!')
else:
    print('Login Incorreto!')