import sqlite3

conexao = sqlite3.connect('bancoteste.db')
cursor = conexao.cursor()

cursor.execute("""SELECT * FROM teste_registro""")
registros = cursor.fetchall()
print(registros)

conexao.commit()
conexao.close()