import mysql.connector

banco = mysql.connector.connect(    #conexão com o banco de dados)
    host = "localhost",
    user = "root",
    password = "123456",
    database = "turmaa"
)
meucursor = banco.cursor()  #usaa as tabelas do banco de dados)
#fetchall recebe tudo da pesquisa e retorna através de uma tupla.
pesquisa = 'select * from alunos'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()
for x in resultado:
    print(x)
nome1 = input("Digite o nome: ")
telefone1 = input("Digite o telefone: ")
sql = "insert into alunos(nome,telefone) values(%s,%s)"
data = (nome1,telefone1)
meucursor.execute(sql,data)
banco.commit()
meucursor.close()
banco.close()

