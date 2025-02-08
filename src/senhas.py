import database
from database import start_db
import sqlite3 as sql
from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colorama import Fore, Style, init # biblioteca para colorir a mensagem no terminal


init()  # Inicializa o colorama

#Romulo Santos Santana

def redefinir_senha():
    while True:
        email_jogador = str(input("\nDigite seu email: "))

        #conexão com o banco de dados
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        try:
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM jogador WHERE email = ?", (email_jogador,))
            
            #   se encontrar o usuario correspondete ao email inserido
            if cursor.fetchone():
                senha_app = "iwkx wwwi agbu xzau"
                
                #   coleta do nome do usuário para inserir no email
                nome = cursor.execute("SELECT nome FROM jogador WHERE email = ?", (email_jogador,)).fetchone()
                nome = nome[0]

                #   criação da nova senha
                nova_senha = randint(10000,99999)
                nova_senha = str(nova_senha)

                #   configuração do servidor para envio do email
                smpt_servidor = "smtp.gmail.com"
                smtp_porta = 587
                smtp_email = "jogoforca.poobj@gmail.com"
                smtp_senha = senha_app

                #   configuração do email
                email_de = "jogoforca.poobj@gmail.com"
                email_para = email_jogador
                assunto_email = "Recuperação de senha"
                corpo_email = f"Oi, {nome}. A sua nova senha é: {nova_senha}\n\nEste é um email automático, não o responda."

                #   atualização da senha
                atualizar_senha = f"UPDATE jogador SET senha = ? WHERE email = ?"
                cursor.execute(atualizar_senha, (nova_senha, email_jogador))
                banco.commit()

                #   criação do email
                email = MIMEMultipart()
                email["From"] = email_de
                email["To"] = email_para
                email["Subject"] = assunto_email
                email.attach(MIMEText(corpo_email, "plain"))
                
                #   envio do email
                servidor = smtplib.SMTP(smpt_servidor, smtp_porta)
                servidor.starttls()
                servidor.login(smtp_email, smtp_senha)
                servidor.sendmail(email_de, email_para, email.as_string())
                servidor.quit()

                #   confirmação
                print("Sua nova senha foi enviada para o email!")
                
            else: 
                print("Email não encontrado. Tente novamente!")   
        finally: # garante o fechamento do banco
            banco.close()
        return
        
# Kauã Conceição Amorim  

def verifica_senha_cpf(cpf_jogador, senha_jogador):
    
    #conexão com o banco de dados
    try: 
        banco = sql.connect(database.start_db.DIRETORIO_FINAL)
        cursor = banco.cursor()
        cursor.execute("SELECT nome, email FROM jogador WHERE senha = ? AND cpf = ?", (senha_jogador, cpf_jogador))
        resultado = cursor.fetchone()
    
        #   se encontrar o usuario correspondente ao cpf e senha inserido
        if resultado: 
            return resultado
        else:
            print(Fore.RED + "\nLogin inválido! Tente novamente.\n" + Style.RESET_ALL)
            return None
    finally:
        banco.close()
    
