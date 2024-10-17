"""try:
    print(x)
except NameError:
    print("Teve problema com a variável!")"""


"""aly="texto"
try:
    print(aly - 2)
except TypeError:
    print("Não pode fazer operação com string!")"""


"""cidades=["Abreu e Lima", "Igarassu"]
try:
    print(cidades[3])
except IndexError:
    print("Índice não encontrado!")"""

"""try:
    populacao = {"Araçoiaba": 100000, "Abreu e Lima": 200000}
except KeyError:
    print("C")"""

from Biblioteca import *  #criar um menu

while True:
    opcao = int(input(f"Qual a sua opção: \n" 
                      "1 para INSERIR;\n" 
                      "2 para MOSTRAR;\n" 
                      "3 para SAIR;\n" 
                      "4 para PESQUISAR;\n"))
    match opcao:
        case 1:
            cadastrar(input("Digite um texto: "))
        case 2:
            mostrar()
        case 3:
            break
        case 4:
            pesquisar(input("Qual a palavra para Pesquisar: "))
        case _:
            print("Opção Iválida!")



