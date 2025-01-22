# Kauã Conceição Amorim

import database
from database import start_db
import sqlite3 as sql

class perguntas():
    def __init__(self, codigo='', dica='', palavra='', max_tentativas=''):
        self.codigo = codigo
        self.dica = dica
        self.palavra = palavra
        self.max_tentativas = max_tentativas
        
    def cadastrar_pergunta(self):
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        cursor = banco.cursor()
        
        while True:
            # Comando sql SELECT COUNT para que o admin veja a quantidade de perguntas já cadastradas
            cursor.execute("SELECT COUNT (*) FROM perguntas")
            quantidade_perguntas = cursor.fetchone()[0]
            print(f"\n\t**Atualmente há {quantidade_perguntas} perguntas cadastradas**\n")
            
            # Aqui o admin insere as informações da pergunta
            
            self.codigo = int(input("Número da pergunta: "))
            
            
            self.dica = input(f"Dica da pergunta {self.codigo}: ").strip()
            self.palavra = input(f"Resposta da dica: {self.dica}: ").strip()
            
            # tratamento de exceção : caso o admin coloque 0 tentativas para o usuário
            while True: 
                try:
                    self.max_tentativas = int(input("Máximo de tentativas do jogador: "))
                    if self.max_tentativas <= 0:
                        print("\n\tO número de tentativas deve ser maior que zero.\n")
                        continue
                    break
                except ValueError:
                    print("\nPor favor, insira um número válido.\n")
            
        # inserção de dados na tabela perguntas a partir do comando INSERT INTO
            cursor.execute(''' INSERT INTO perguntas (codigo, dica, palavra, max_tentativas)            
            VALUES(?,?,?,?)''',(self.codigo, self.dica, self.palavra, self.max_tentativas))
        
            banco.commit()
            print('\nInformações inseridas com sucesso!\n')
            
            escolha = input("\nDeseja inserir mais perguntas? [S/N]: \n").strip().upper()
            
            if escolha != 'S':
                break
            else:
                pass # O loop continua para cadastrar mais dados na tabela perguntas

        # fecha o banco de dados
        banco.close()  
          