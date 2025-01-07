#Romulo Santos Santana

import requests

def menu_principal():

    opcoes = [1, 2, 3, 4, 5]

    print("-"*45)
    print("\t1. Jogar")
    print("\t2. Cadastrar novo usuário")
    print("\t3. Recuperar senha")
    print("\t4. Entrar como administrador")
    print("\t5. Sair")
    print("-"*45)

    while True:
        opcao = int(input("\tDigite a opção desejada: "))
        if opcao in opcoes:
            return opcao

class Jogador():
    def __init__(self, cpf = "", nome = "", email = "", idade = "", endereco = "", senha = ""):

        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.idade = idade
        self.endereco = endereco
        self.senha = senha

    def validar_cpf(self):
        pass

    def inserir_nome(self):
        while True:
            self.nome = str(input("Digite o nome: "))
            nome_valido = self.nome.strip().replace(" ", "")

            if nome_valido.isalpha():
                return self.nome.upper()
            else:
                print("Existem caracteres inválidos ou o nome está em branco. Digite novamente.")

        