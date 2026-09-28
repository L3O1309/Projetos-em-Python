"""Aprendendo SQLite3. Comandos básicos 
aplicados a um teste para um futuro projeto"""
import sqlite3

conexao = sqlite3.connect('bancoteste.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS teste_registro(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                senha_sem_criptografia TEXT NOT NULL)""") #Cria a tabela teste_registro, se não existir

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    senha_sem_criptografia = input("Digite a senha: ")

    cursor.execute("""INSERT INTO teste_registro
                    (nome, email, senha_sem_criptografia) VALUES
                    (?, ?, ?)""", (nome, email, senha_sem_criptografia))
#Função para cadastro na tabela
cadastrar_aluno() #Chama a função para executar 

conexao.commit()
conexao.close()
