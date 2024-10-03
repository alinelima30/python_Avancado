#Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes,
#e que exiba a lista desses nomes na tela. Após exibir essa lista,
#o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.

names = [0] *5
tam = len(names)
for x in range(tam):
    names[x] = input(f"Digite o {x+1}º Nome: ")
for i in range(tam):
    print(names[i], end = "|")
print()
for j in range(tam-1,-1,-1):
    print(names[j])