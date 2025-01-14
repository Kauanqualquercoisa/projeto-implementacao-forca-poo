
import database
import sqlite3 as sql
import database.start_db


def verificar_senha_cpf():
    
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
        
        Digite sua Opção:
        
        '''
        
        print(mensagem)
    else:
        print('login inválido')
if __name__ == "__main__":
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
        
        Digite sua Opção:
        
        '''
        
        print(mensagem)
    else:
        print('login inválido')
    
    
