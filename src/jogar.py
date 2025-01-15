import random
import sqlite3

def sortear_pergunta():
    banco = sqlite3.connect('database/jogo.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM perguntas")
    
    perguntas = cursor.fetchall()
    
    if perguntas:
        # Escolhe uma pergunta aleatória
        pergunta_aleatoria = random.choice(perguntas)
        banco.close()  # Fecha a conexão com o banco
        return pergunta_aleatoria  # Retorna a pergunta sorteada
    else:
        banco.close()
        return None  # Caso não existam perguntas no banco
    
    