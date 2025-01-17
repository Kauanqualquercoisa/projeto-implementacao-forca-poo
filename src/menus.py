import functions
from functions import Jogador
import sqlite3 as sql
import redefinir_senha
from redefinir_senha import redefinir_senha
import database
from database import start_db
import verificar_s_c
from perguntas import *

def menu_principal():

    print("\n" + "-"*15 + " MENU PRINCIPAL " + "-"*15)
    print("\t1. Jogar\n\t2. Cadastrar novo usuário\n\t3. Recuperar senha\n\t4. Entrar como administrador\n\t5. Sair")
    print("-"*46)

    opcoes = [1, 2, 3, 4, 5]
    opcao = int(input("\tDigite a opção desejada: "))

    if opcao in opcoes:
        if opcao == 1:
            verificar_s_c.verificar_s_c()
        elif opcao == 2:
            novo_usuario = Jogador()
            novo_usuario.cadastrar_usuario()
            menu_principal()
        elif opcao == 3:
            redefinir_senha()
            menu_principal()
        elif opcao == 4:
            entrar_como_administrador()
            menu_principal
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
            pergunta = cadastrar_pergunta()
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            menu_principal()
    print("Digite uma opção válida!")

