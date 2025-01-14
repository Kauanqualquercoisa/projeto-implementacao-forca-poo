import functions
from functions import Jogador
import sqlite3 as sql
import redefinir_senha
from redefinir_senha import redefinir_senha
import database

def menu_principal():

    print("-"*15+" MENU PRINCIPAL "+"-"*15)
    print("\t1. Jogar\n\t2. Cadastrar novo usuário\n\t3. Recuperar senha\n\t4. Entrar como administrador\n\t5. Sair")
    print("-"*46)

    opcoes = [1, 2, 3, 4, 5]
    opcao = int(input("\tDigite a opção desejada: "))

    if opcao in opcoes:
        if opcao == 1:
            pass
        elif opcao == 2:
            novo_usuario = Jogador()
            novo_usuario.cadastrar_usuario()
            menu_principal()
        elif opcao == 3:
            redefinir_senha()
            menu_principal()
        elif opcao == 4:

            menu_administrador()
            menu_principal
        elif opcao == 5:
            print("\tObrigado por jogar!")
            return
    print("Digite uma opção válida!")
    menu_principal()


def menu_administrador():
    print("-"*15+" MENU ADMINISTRADOR "+"-"*15)
    print("\t1. Jogar\n\t2. Cadastrar novo usuário\n\t3. Recuperar senha\n\t4. Entrar como administrador\n\t5. Sair")
    print("-"*60)
    
    
def entrar_como_administrador():
    login = str(input("Digite o login de administrador: "))
    senha = str(input("Digite a senha de administrador: "))

    banco = sql.connect(database.start_db.DIRETORIO_FINAL)
    cursor = banco.cursor()
    cursor.execute

