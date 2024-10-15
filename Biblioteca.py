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
        return numero, "Não é primo"
    elif numero == 2:
        return numero, "É primo"
    else:
        for x in range(2,numero):
            if (numero % x==0):
                return numero, "Não é primo"
            return numero, "É primo"""

class Pessoa:
    def __init__(self,nome,peso,idade): #método_construtor
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.andando=False
        self.dormindo=False
    def comer(self):
        if self.comendo == False:
            if self.andando == False:
                if self.dormindo == False:
                    print(f"{self.nome}, Foi comer!")
                    self.comendo = True
                else:
                    print(f"{self.nome}, Não pode comer pois está dormindo!")
            else:
                print(f"{self.nome}, Não pode comer pois está andando!")
        else:
            print(f"{self.nome}, já estava comendo!")
    def andar(self):
        if self.andando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome} Foi andar!")
                    self.andando = True
                else:
                    print(f"{self.nome}, Não pode andar pois está dormindo!")
            else:
                print(f"{self.nome}, Não pode andar pois está comendo!")
        else:
            print(f"{self.nome}, Já estava andando!")

class Animal:
    def __init__(self,nome,cor):
        self.nome =nome
        self.cor =cor
    def comer(self):
            print(f"O {self.nome}: Está comendo!")

class Gato(Animal):
    def __init__(self,nome,cor):
     super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome}: Está miando! ")











