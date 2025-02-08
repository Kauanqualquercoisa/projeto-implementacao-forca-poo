# Kauã Conceição Amorim e Amanda Frasson

import database
from database import start_db
import sqlite3 as sql
import csv
import random
import os


class Perguntas():
    def __init__(self, codigo='', dica='', palavra='', max_tentativas='', perguntas_csv=''):
        self.codigo = codigo
        self.dica = dica
        self.palavra = palavra
        self.max_tentativas = max_tentativas
        # self.perguntas_csv= perguntas_csv
        
# Kauã Conceição Amorim

    def cadastrar_pergunta(self):
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        cursor = banco.cursor()

        while True:
            # Comando sql SELECT COUNT para que o admin veja a quantidade de perguntas já cadastradas
            cursor.execute("SELECT COUNT (*) FROM perguntas")
            quantidade_perguntas = cursor.fetchone()[0]
            print(
                f"\n\t**Atualmente há {quantidade_perguntas} perguntas cadastradas**\n")

            # Aqui o admin insere as informações da pergunta

            self.codigo = int(input("Número da pergunta: "))

            self.dica = input(f"Dica da pergunta {self.codigo}: ").strip()
            self.palavra = input(f"Resposta da dica: {self.dica}: ").strip()

            # tratamento de exceção : caso o admin coloque 0 tentativas para o usuário
            while True:
                try:
                    self.max_tentativas = int(
                        input("Máximo de tentativas do jogador: "))
                    if self.max_tentativas <= 0:
                        print("\n\tO número de tentativas deve ser maior que zero.\n")
                        continue
                    break
                except ValueError:
                    print("\nPor favor, insira um número válido.\n")

        # inserção de dados na tabela perguntas a partir do comando INSERT INTO
            cursor.execute(''' INSERT INTO perguntas (codigo, dica, palavra, max_tentativas)            
            VALUES(?,?,?,?)''', (self.codigo, self.dica, self.palavra, self.max_tentativas))

            banco.commit()
            print('\nInformações inseridas com sucesso!\n')

            escolha = input(
                "\nDeseja inserir mais perguntas? [S/N]: \n").strip().upper()

            if escolha != 'S':
                print("\nVoltando para o menu administrador...\n")
                banco.close()
                return
            else:
                pass  # O loop continua para cadastrar mais dados na tabela perguntas

            # fecha o banco de dados
            banco.close()
            
# Amanda Frasson

    def exportar_para_csv(self, perguntas_csv=''):
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        cursor = banco.cursor()

        opcao = str(input("\nDeseja exportar os dados das perguntas? [S/N] "))
        tipo_opcoes = ['S', 's', 'sim', 'SIM']

        if opcao in tipo_opcoes:
            try:
                # Consultar todos os dados da tabela perguntas
                cursor.execute("SELECT * FROM perguntas")
                dados = cursor.fetchall()  # Obtém todos os registros
                colunas = [descricao[0]
                           # Nomes das colunas
                           for descricao in cursor.description]

                # Criar o arquivo CSV e escrever os dados
                with open(perguntas_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:
                    escritor_csv = csv.writer(
                        arquivo_csv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Escrever o cabeçalho (nomes das colunas)
                    escritor_csv.writerow(colunas)
                    # Escrever os dados
                    escritor_csv.writerows(dados)

            except sql.Error:
                print(f"Erro ao exportar dados")
        banco.close()

    def listar_perguntas(self, numero_pergunta):
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        cursor = banco.cursor()
        while True:
            # Comando sql SELECT COUNT para que o admin veja a quantidade de perguntas já cadastradas
            cursor.execute("SELECT COUNT (*) FROM perguntas")
            quantidade_perguntas = cursor.fetchone()[0]
            print(
                f"\n\t**Atualmente há {quantidade_perguntas} perguntas cadastradas**\n")

            # exibindo todas as perguntas
            cursor.execute("SELECT * FROM perguntas")
            lista_perguntas = cursor.fetchall()
            print("\t**Lista de perguntas cadastradas:**")
            tam = len(lista_perguntas)
            for i in range(tam):
                print(lista_perguntas[i])
            break
        if numero_pergunta == '0':
            self.exportar_para_csv('perguntas_csv')
            return

    def atualizar_pergunta(self):
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        cursor = banco.cursor()

        funcao_listar = Perguntas()
        funcao_listar.listar_perguntas(numero_pergunta='1')

        self.codigo = int(
            input("\n\nQual o número da pergunta que deseja atualizar? "))
        cursor.execute(
            "SELECT codigo FROM perguntas WHERE codigo = ?", (self.codigo,))
        resultado = cursor.fetchone()

        if resultado:
            # Definindo os novos dados
            dica2 = input(f"Dica da pergunta {self.codigo}: ").strip()
            palavra2 = input("Resposta da dica(palavra): ").strip()

            # tratamento de exceção : caso o admin coloque 0 tentativas para o usuário
            while True:
                try:
                    max_tentativas2 = int(
                        input("Máximo de tentativas do jogador: "))
                    if max_tentativas2 <= 0:
                        print("\n\tO número de tentativas deve ser maior que zero.\n")
                        continue
                    break
                except ValueError:
                    print("\nPor favor, insira um número válido.\n")

            # Busca os dados anteriores
            cursor.execute(
                "SELECT dica, palavra, max_tentativas FROM perguntas WHERE codigo = ?", (self.codigo,))
            resultado = cursor.fetchone()
            if resultado:
                self.dica = resultado[0]
                self.palavra = resultado[1]
                self.max_tentativas = resultado[2]

            cursor.execute("""UPDATE perguntas SET dica = ?, palavra = ?, max_tentativas = ? 
                        WHERE dica = ? AND palavra = ? AND max_tentativas = ?  """, (dica2, palavra2, max_tentativas2, self.dica, self.palavra, self.max_tentativas))  # (novo_nome, nome_atual)

            banco.commit()
            print('\nInformações atualizadas com sucesso!\n')
        else:
            print("\nO número da pergunta não existe.\n")

        banco.close()

    def remover_pergunta(self):
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        cursor = banco.cursor()

        funcao_listar = Perguntas()
        funcao_listar.listar_perguntas(numero_pergunta='2')

        self.codigo = int(
            input("\n\nQual o número da pergunta que deseja remover? "))
        cursor.execute(
            "SELECT codigo FROM perguntas WHERE codigo = ?", (self.codigo,))
        resultado = cursor.fetchone()

        if resultado:
            cursor.execute(
                "DELETE FROM perguntas WHERE codigo = ?", (self.codigo,))
            banco.commit()
            print(f"\nA pergunta {self.codigo} foi removida com sucesso.\n")

            # Atualizar os códigos para manter a sequência correta
            cursor.execute("SELECT codigo FROM perguntas ORDER BY codigo")
            perguntas = cursor.fetchall()

            novo_codigo = 1
            for pergunta in perguntas:
                cursor.execute(
                    "UPDATE perguntas SET codigo = ? WHERE codigo = ?", (novo_codigo, pergunta[0]))
                novo_codigo += 1

            banco.commit()

        else:
            print("\nEsta pergunta não existe.\n")

        banco.close()
        
# Kauã Conceição Amorim

    def sortear_pergunta(self):
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        cursor = banco.cursor()
        cursor.execute("SELECT dica, palavra, max_tentativas FROM perguntas")

        dados = cursor.fetchall()  # verifica se há perguntas no banco de dados

        if dados:
            cursor.execute("SELECT COUNT (*) FROM perguntas")
            quantidade_perguntas = cursor.fetchone()[0]

            # Escolhe uma pergunta aleatória

            # posição_aleatoria recebe uma valor qualquer no range de 0 até o total de perguntas cadastradas
            posicao_aleatoria = random.randint(0, quantidade_perguntas-1)

            linha_aleatoria = dados[posicao_aleatoria]
            self.dica, self.palavra, self.max_tentativas = linha_aleatoria

        else:
            print("\nNão tem perguntas no banco de dados\n")
            return None  # Caso não existam perguntas no banco

        banco.close()
