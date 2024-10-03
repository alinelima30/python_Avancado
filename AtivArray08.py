#Faça um código para ler 5 nomes de usuários e suas respectivas senhas,
# e armazenar cada lista em um array diferente, após completar a digitação,
# imprimir, nome, senha e posição dos dados no array.

names = [0] * 5
senha = [0] * 5
tam = len(names)
for x in range(tam):
    names[x] = input("Digite Seu nome: ")
    senha[x] = int(input("Digite Sua Senha: "))
for j in range(tam):
    print(names[j],senha[j],[j])

