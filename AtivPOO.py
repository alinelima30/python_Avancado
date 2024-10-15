"""from Biblioteca import *
p1 = Pessoa("Lili",60,22)
p1.comer()
p1.comer()
p1.andar()
"""

from Biblioteca import *
p1 = Animal("Leão","Branco com pintas marrons")
p1.comer()

from Biblioteca import *
a1 = Gato("Mimi", "Pretinho")
a1.miar()

#complete este exercício sobre
# herança, criando as classes cachorro, coelho e vaca, herdando da Classe Animal. +(polimorfismo - comer)

from Biblioteca import *
a1 = Cachorro("Sansão", "Black")
a1.comer()
a1.latir()

from Biblioteca import *
a1 = Coelho("Ig", "Malhado")
a1.chiar()

from Biblioteca import *
c1 = Corredor("Joy", 65)
c1.aposentar()
c1.aquecer()
c1.correr()
t1 = TriAtleta("Joy", 22)
t1.nadar()