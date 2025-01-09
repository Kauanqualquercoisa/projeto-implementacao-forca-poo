#Romulo Santos Santana

import sqlite3 as sql
import os

#   definição do diretório no qual o banco de dados vai ser criado
DIRETORIO_RAIZ = os.getcwd()
DIRETORIO_FINAL = os.path.join(DIRETORIO_RAIZ,"src", "database", "jogo_forca.db")

#   conexão do banco de dados e criação do cursor
banco = sql.connect(DIRETORIO_FINAL)
cursor = banco.cursor()

#   criação das tabelas
cursor.execute("""CREATE TABLE IF NOT EXISTS administrador(
               nome text, 
               email text,
               login text,
               senha text)
               """)

cursor.execute("""CREATE TABLE IF NOT EXISTS jogador(
               cpf text,
               nome text,
               idade text,
               endereco text,
               email text,
               senha text)
               """)

cursor.execute("""CREATE TABLE IF NOT EXISTS perguntas(
               codigo INTEGER PRIMARY KEY AUTOINCREMENT,
               dica text,
               palavra text,
               max_tentativas integer)
               """)

#   inserção do administrador

# cursor.execute("""INSERT INTO administrador (nome, email, login, senha)
#                VALUES ("ROMULO", "romulo.ssant@gmail.com", "admin", "admin")""")


banco.commit()
banco.close()