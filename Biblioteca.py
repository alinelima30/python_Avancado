


def imprimir_nome(nome):
    print(f"Nome: {nome}")
    imprimir_nome("Erickson")
    imprimir_nome("Renan")
    imprimir_nome("Daniel")

def imprimir_numeros(n):
    for x in range(1,n+1,1):
        print(x, end = " ")

def somar(n1,n2,n3,n4,n5):
    soma= n1+n2+n3+n4+n5
    print(soma)

def adicao(*numeros):
    adicao = 0
    for x in (numeros):
        adicao+= x
    print(adicao)

def texto(texto):
    cont=0
    for i in texto:
        if i not in " ":
            cont+=1
    print(f"A quantidade do texto é: {cont}")
    tam = len(texto)
    for x in range(tam - 1, -1, -1):
        print(texto[x], end="")

def listaUnica(a):
    nova_lista=[]
    for x in a:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

def num_primo(numero):
    if numero == 1:
        print("Não é Primo")
    elif numero == 2:
        print("É Primo")
    else:
        for x in range(2,numero):
            if (numero % x==0):
                print("Não é Primo")
                break
            print("É primo")
            break








