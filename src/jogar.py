import database
from database import start_db
import sqlite3 as sql
import random


def sortear_pergunta():
    banco = sql.connect(database.start_db.DIRETORIO_FINAL)
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM perguntas")

    perguntas = cursor.fetchall()

    if perguntas:
        # Escolhe uma pergunta aleatória
        pergunta_aleatoria = random.choice(perguntas)
        banco.close()  # Fecha a conexão com o banco
        return pergunta_aleatoria  # Retorna a pergunta sorteada
    else:
        print("\nNão tem perguntas no banco de dados\n")
        banco.close()
        return None  # Caso não existam perguntas no banco
