# Kauã Conceição Amorim

import database
from database import start_db
import sqlite3 as sql
import random


def sortear_pergunta():
    banco = sql.connect(database.start_db.DIRETORIO_FINAL)
    cursor = banco.cursor()
    cursor.execute("SELECT dica, palavra, max_tentativas FROM perguntas")

    dados = cursor.fetchall()  # verifica se há perguntas no banco de dados

    if dados:
        cursor.execute("SELECT COUNT (*) FROM perguntas")
        quantidade_perguntas = cursor.fetchone()[0]

        # Escolhe uma pergunta aleatória

        # posição_aleatoria recebe uma valor qualquer no range de 0 até o total de perguntas cadastradas
        posicao_aleatoria = random.randint(0, quantidade_perguntas)

        linha_aleatoria = dados[posicao_aleatoria]
        dica, palavra, max_tentativas = linha_aleatoria

        mensagem = f'''
        ------------------ Jogo da Forca -----------------

        Dica:{dica}

        Palavra: _______({palavra})

        Tentativas: Tentativas Restantes / Total Tentativas:{max_tentativas}

            Fale uma letra:           '''

        print(mensagem)

    else:
        print("\nNão tem perguntas no banco de dados\n")
        banco.close()
        return None  # Caso não existam perguntas no banco
