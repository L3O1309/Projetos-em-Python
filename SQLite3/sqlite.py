import sqlite3

conexao = sqlite3.connect('bancoteste.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS teste_registro(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                senha_sem_criptografia TEXT NOT NULL)""")

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    senha_sem_criptografia = input("Digite a senha: ")

    cursor.execute("""INSERT INTO teste_registro
                    (nome, email, senha_sem_criptografia) VALUES
                    (?, ?, ?)""", (nome, email, senha_sem_criptografia))

cadastrar_aluno()
cursor.execute("SELECT * FROM teste_registro")


conexao.commit()
conexao.close()