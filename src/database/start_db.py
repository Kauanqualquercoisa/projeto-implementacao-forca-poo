#Romulo Santos Santana

import sqlite3 as sql
import os

DIRETORIO_RAIZ = os.getcwd()
DIRETORIO_FINAL = os.path.join(DIRETORIO_RAIZ,"src", "database", "jogo_forca.db")

print(DIRETORIO_FINAL)

banco = sql.connect(DIRETORIO_FINAL)
cursor = banco.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS administrador(
               nome text, 
               email text,
               login text,
               senha text)
               """)

cursor.execute("""CREATE TABLE IF NOT EXISTS jogador(
               cpf text NOT NULL UNIQUE,
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

# cursor.execute("""INSERT INTO administrador (nome, email, login, senha)
#                VALUES ("ROMULO", "romulo.ssant@gmail.com", "admin", "admin")""")

banco.commit()
banco.close()