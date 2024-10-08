rep=0
opcao=0
pin=0
nome=[0]
senha=[0]
tam=len(nome)
while opcao !=4 and rep <=3:
	print("<<" * 10)
	print(" [1] para Cadastrar;\n [2] para Mostrar Cadastro;\n [3] para Login;\n [4] para Sair;")
	print("<<" * 10)
	opcao = int(input("Escolha uma Opção: "))
	print("<<" * 10)
	if opcao ==1:
		for x in range(tam):
			nome[x]= input("Digite seu Nome: ")
			senha[x]= int(input("Digite sua Senha: "))
	elif opcao ==2:
		for j in range(tam):
			print(f"Nome:{nome[j]} Senha:{senha[j]} Posição:{[j]}")
	elif opcao ==3:
		usuario= input("Usuário: ")
        pin= int(input("Senha: "))
        for i in range(tam):
            if usuario != opcao ==1:
                print("Usuario Inválido!")
            elif senha != opcao ==1:
                print("Senha Inválida!")