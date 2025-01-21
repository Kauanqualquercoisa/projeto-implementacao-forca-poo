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
    cursor.execute("SELECT nome, email FROM jogador WHERE senha = ? AND cpf = ?", (senha_jogador, cpf_jogador))
    resultado = cursor.fetchone()
 

    #   se encontrar o usuario correspondete ao cpf e senha inserido
    if resultado:  
        # Se o jogador for encontrado
        nome_jogador = resultado[0] #coloca o nome do jogador
        email_jogador= resultado[1]

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
                mensagem2 = f"""\nAtualizar Dados
                        1 - Nome: {nome_jogador}
                        2 - CPF: {cpf_jogador}
                        3 - Senha: {senha_jogador}
                        4 - Email: {email_jogador}
                        5 - Sair"""
                print(mensagem2)
                    
                atualiza = int(input("\nDigite uma das opções que deseja alterar: "))

                while atualiza != 5:
                    if atualiza == 1:
                        nome_jogador2 = input("Digite o novo nome: ")
                        cursor.execute("""UPDATE jogador SET nome = ? WHERE nome = ?  """, (nome_jogador2, nome_jogador))#(novo_nome, nome_atual)
                        # Confirmar as mudanças
                        banco.commit()
                        print("Nome atualizado com sucesso!")

                        atualiza = int(input("\nDigite a outra opção ou 5 para sair: "))

                    elif atualiza == 2:
                        cpf_jogador2 = input("Digite um novo cpf: ")
            
                        cursor.execute("""UPDATE jogador SET cpf = ? WHERE cpf = ?  """, (cpf_jogador2, cpf_jogador))
                        banco.commit()
                        print("Cpf atualizado com sucesso!")
                        atualiza = int(input("\nDigite a outra opção ou 5 para sair: "))

                    elif atualiza == 3:
                        senha_jogador2 = input("Digite uma nova senha: ")
            
                        cursor.execute("""UPDATE jogador SET senha = ? WHERE senha = ?  """, (senha_jogador2, senha_jogador))
                        banco.commit()
                        print("Senha atualizado com sucesso!")
                        atualiza = int(input("\nDigite a outra opção ou 5 para sair: "))

                    elif atualiza == 4:
                        email_jogador2 = input("Digite o novo email:  ")
            
                        cursor.execute("""UPDATE jogador SET email = ? WHERE email = ?  """, (email_jogador2, email_jogador))
                        banco.commit()
                        print("Email atualizado com sucesso!")
                        atualiza = int(input("\nDigite a outra opção ou 5 para sair: "))

                if atualiza == 5:
                    print("Voltando para o menu principal")

            case 3:
                print('Voltando para o menu principal\n')
                
            case _:
                print('Opção inválida\n')
    else:
        print(Fore.RED + "\nLogin inválido! Tente novamente.\n" + Style.RESET_ALL)
