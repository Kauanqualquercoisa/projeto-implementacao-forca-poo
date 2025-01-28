# Amanda Frasson e Kauã Conceição Amorim

import database
import sqlite3 as sql
import database.start_db
from menus import *
from senhas import verifica_senha_cpf
from colorama import Fore, Style, init # biblioteca para colorir a mensagem no terminal
import pyttsx3 # Importa a biblioteca para TTS (texto para fala)
from atualiza_dados import *
from perguntas import *
from jogador import Jogador
from forca import *


init()  # Inicializa o colorama

# Configuração do pyttsx3
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    

def menu_jogador(resultado):
    
    # Se o jogador for encontrado
    nome_jogador = resultado[0] #recebe o nome do jogador
    email_jogador= resultado[1] #recebe o email do jogador

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
    
    return opcao, nome_jogador, email_jogador

def opcoes_menu():
    cpf_jogador = str(input("\nDigite seu CPF: "))
    senha_jogador = str(input("\nDigite seu senha: "))    

    resultado = verifica_senha_cpf(cpf_jogador,senha_jogador)

    if resultado != None:
        opcao, nome_jogador, email_jogador = menu_jogador(resultado)
        
        match opcao:
            case 1:
                pergunta = Perguntas()
                pergunta.sortear_pergunta()
                
                jogo_forca()
                            
            case 2:
                atualizar_dados(nome_jogador,cpf_jogador,senha_jogador,email_jogador)
                        
            case 3:
                print('Voltando para o menu principal\n')
                        
            case _:
                print('Opção inválida\n')
    else:
        menu_principal()