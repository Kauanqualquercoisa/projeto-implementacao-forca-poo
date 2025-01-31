import jogador
from jogador import Jogador
import sqlite3 as sql
import senhas
import menu_jogo
import database
from database import start_db
from perguntas import *

def menu_principal():

    print("\n" + "-"*15 + " MENU PRINCIPAL " + "-"*15)
    print("\t1. Jogar\n\t2. Cadastrar novo usuário\n\t3. Recuperar senha\n\t4. Entrar como administrador\n\t5. Sair")
    print("-"*46)

    opcoes = [1, 2, 3, 4, 5]
    opcao = int(input("\tDigite a opção desejada: "))

    if opcao in opcoes:
        if opcao == 1:
            menu_jogo.opcoes_menu()
        elif opcao == 2:
            novo_usuario = Jogador()
            novo_usuario.cadastrar_usuario()
            menu_principal()
        elif opcao == 3:
            senhas.redefinir_senha()
            menu_principal()
        elif opcao == 4:
            entrar_como_administrador()
            menu_principal()
        elif opcao == 5:
            print("\tObrigado por jogar!")
            return
    else:
        print("Digite uma opção válida!")
    menu_principal()

def entrar_como_administrador():
    login = str(input("\nDigite o login de administrador: "))
    senha = str(input("Digite a senha de administrador: "))
    print("")

    banco = sql.connect(database.start_db.DIRETORIO_FINAL)
    cursor = banco.cursor()
    entrar_adm = f"SELECT * FROM administrador WHERE login = ? AND senha = ?"
    cursor.execute(entrar_adm, (login, senha))

    if cursor.fetchall():
        menu_administrador()
    else: 
        print("Usuário não encontrado!")
        menu_principal()

def menu_administrador():
    print("\n"+"-"*15+" MENU ADMINISTRADOR "+"-"*15)
    print("\t1. Cadastrar nova pergunta\n\t2. Atualizar pergunta\n\t3. Remover pergunta\n\t4. Listar perguntas\n\t5. Voltar ao menu principal")
    print("-"*50)

    opcoes = [1, 2, 3, 4, 5]
    opcao = int(input("\tDigite a opção desejada: "))

    if opcao in opcoes:
        if opcao == 1:
            pergunta = Perguntas()
            pergunta.cadastrar_pergunta()
        elif opcao == 2:
            pergunta = Perguntas()
            pergunta.atualizar_pergunta()
            
        elif opcao == 3:
            pergunta = Perguntas()
            pergunta.remover_pergunta()
            
        elif opcao == 4:
            pergunta = Perguntas()
            pergunta.listar_perguntas()
            
        elif opcao == 5:
            menu_principal()
        else:
            print("Digite uma opção válida!")

