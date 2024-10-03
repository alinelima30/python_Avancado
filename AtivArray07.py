#Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números,
# o código deve escrever esses 5 números lidos na ordem inversa.

num = [0] * 5
tam = len(num)
for x in range(tam):
    num[x] = int(input("Digite um Número: "))
for j in range(tam-1,-1,-1):
    print(num[j], end = "")
