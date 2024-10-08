#Faça um algoritmo que leia 10 valores do tipo inteiro e armazene-os em um vetor. A seguir,
#o algoritmo deverá informar: (1) todos os números pares que existem no vetor.
#(2) o menor e o maior valor existente no vetor.
#(3) quantos dos valores do vetor são maiores que a média desses valores.

num = [0] * 10
tam = len(num)
maior = 0
menor = 0
media = 0

for x in range(tam):
    num[x] = int(input(f"Digite o {x+1}º Valor: "))
print()
for i in range(tam):
    if (num[i] % 2) == 0:
        print(f"Quantos Números Par tem: {i}")
for j in range(tam):






