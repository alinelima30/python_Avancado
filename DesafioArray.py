opcao = 0
rep = 0
usuarios = []
senhas = []

while opcao != 4 and rep < 3:
    print("<<" * 15)
    print("MENU:\n 1. Para Cadastro;\n 2. Mostrar Cadastro;\n 3. Para Login;\n 4. Sair.")
    print("<<" * 15)
    opcao = int(input("Escolha Uma Opção: "))
    print("<<" * 15)

    if opcao == 1:
        print("Cadastro:\n")
        usuario = input("Digite Seu Nome: ")
        senha = int(input("Digite Sua Senha: "))
        usuarios.append(usuario)
        senhas.append(senha)
    elif opcao == 2:
        print("Mostrar Cadastro:\n")
        for y in range(len(usuarios)):
            print(f"Usuário: {usuarios[y]} | Senha: {senhas[y]} | Posição: {y}")
    elif opcao == 3:
        print("Login:\n")
        usuario = input("Digite Seu Nome de Usuário: ")
        senha = int(input("Digite Sua Senha: "))
        if usuario in usuarios:
            indice = usuarios.index(usuario)
            if senhas[indice] == senha:
                print(f"{usuario}, Login Efetuado Com Sucesso!")
                rep = 0  
            else: 
                print("Senha Incorreta!")
                rep += 1
        else:
            print("Usuário Não Encontrado!")
            rep += 1
    elif opcao == 4:
        print("Você Saiu Do Programa!")
    else:
        print("Opção Inválida, Tente Novamente!")

if rep >= 3:
    print("Acesso Bloqueado!")

print("Você Saiu do programa!")
