# Amanda Frasson

import database
from database import start_db
import sqlite3 as sql


def atualizar_dados(nome_jogador,cpf_jogador,senha_jogador,email_jogador):
    banco = sql.connect(database.start_db.DIRETORIO_FINAL)
    cursor = banco.cursor()
    
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
    
    banco.close()