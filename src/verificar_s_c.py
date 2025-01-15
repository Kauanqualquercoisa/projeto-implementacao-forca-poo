import database
import sqlite3 as sql
import database.start_db
from menus import *


def verificar_s_c():
    
    cpf_jogador = str(input("\nDigite seu CPF: "))
    senha_jogador = str(input("\nDigite seu senha: "))

    #conexão com o banco de dados
    banco = sql.connect(database.start_db.DIRETORIO_FINAL)
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM jogador WHERE senha = ? AND cpf = ?", (senha_jogador, cpf_jogador))

    #   se encontrar o usuario correspondete ao cpf e senha inserido
    if cursor.fetchone():
        # menu do jogo
        mensagem = ''' 
        --------- Menu Jogo da Forca – anonimo --------
        1 – Jogar
        2 – Atualizar Dados
        3 – Voltar Menu Principal
        
        '''
        
        print(mensagem)
        
        opcao = int(input("Digite sua Opção: "))
        
        match opcao:
            case 1:
                print('Jogar\n')
            case 2:
                print('Atualizar Dados\n')
            case 3:
                print('Voltando para o Menu Principal\n')
                
            case _:
                print('Opção inválida\n')
    else:
        print('login inválido\n')
