# Amanda Frasson e Kauã Conceição Amorim

import database
import sqlite3 as sql
import database.start_db
from menus import *
from colorama import Fore, Style, init # biblioteca para colorir a mensagem no terminal
import pyttsx3 # Importa a biblioteca para TTS (texto para fala)
from jogar import *

init()  # Inicializa o colorama

# Configuração do pyttsx3
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    
def verificar_s_c():
    
    cpf_jogador = str(input("\nDigite seu CPF: "))
    senha_jogador = str(input("\nDigite seu senha: "))

    #conexão com o banco de dados
    banco = sql.connect(database.start_db.DIRETORIO_FINAL)
    cursor = banco.cursor()
    cursor.execute("SELECT nome FROM jogador WHERE senha = ? AND cpf = ?", (senha_jogador, cpf_jogador))
    resultado = cursor.fetchone()
    
    #   se encontrar o usuario correspondete ao cpf e senha inserido
    if resultado:  
        # Se o jogador for encontrado
        nome_jogador = resultado[0] #coloca o nome do jogador
        
        print(Fore.GREEN + "\nLogin realizado com sucesso!\n" + Style.RESET_ALL)
        
        mensagem = f"\nBem-vindo, {nome_jogador}!\n"
        
        print(mensagem)  
        falar(mensagem)  #Fala a mensagem em áudio
        
        
        
        # menu do jogo
        mensagem = f'''
        --------- Menu Jogo da Forca – {nome_jogador} --------
        1 – Jogar
        2 – Atualizar Dados
        3 – Voltar Menu Principal
        
        '''
        
        print(mensagem)
        
        opcao = int(input("Digite sua Opção: "))
        
        match opcao:
            case 1:
                pergunta = sortear_pergunta()
                print(pergunta)
            case 2:
                print('Atualizar Dados\n')
                
            case 3:
                print('Voltando para o Menu Principal\n')
                
            case _:
                print('Opção inválida\n')
    else:
        print(Fore.RED + "\nLogin inválido! Tente novamente.\n" + Style.RESET_ALL)
