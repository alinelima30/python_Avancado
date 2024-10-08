def imprimir_nome(nome):
    print(f"Nome: {nome}")
    imprimir_nome("Erickson")
    imprimir_nome("Renan")
    imprimir_nome("Daniel")
def imprimir_numeros(n):
    for x in range(1,n+1,1):
        print(x, end = " ")