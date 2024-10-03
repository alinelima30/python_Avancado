#Faça um código para ler 10 números e guardar num vetor. Após isto,
#ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

numero = [0] *10
tam = len(numero)
cont = 0
for x in range(tam):
    numero[x] = int(input(f"Digite o {x+1} Número: "))
num = int(input("Digite mais um número: "))
for i in range(tam):
   if num == numero[i]:
    cont+=1
print(f"O número {num} aparece {cont} vezes!")

