import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "turmaa"
)
meucursor = banco.cursor()
pesquisa = 'select * from funcionario'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()
for x in resultado:
    print(x)
meucursor.close()
banco.close()

