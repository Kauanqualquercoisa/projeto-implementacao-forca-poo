#Romulo Santos Santana

import requests
import sqlite3 as sql

def menu_principal():

    opcoes = [1, 2, 3, 4, 5]

    print("-"*45)
    print("\t1. Jogar")
    print("\t2. Cadastrar novo usuário")
    print("\t3. Recuperar senha")
    print("\t4. Entrar como administrador")
    print("\t5. Sair")
    print("-"*45)

    opcao = int(input("\tDigite a opção desejada: "))

    if opcao not in opcoes:
        print("Digite uma opção válida!")
        menu_principal()

    else:
        if opcao == 1:
            pass
        elif opcao == 2:
            novo_usuario = Jogador()
            novo_usuario.cadastrar_usuario()
            menu_principal()
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            print("\tObrigado por jogar!")
            return
      
class Jogador():
    def __init__(self, cpf = "", nome = "", email = "", idade = "", cep = "", endereco = "", senha = ""):

        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.idade = idade
        self.cep = cep
        self.endereco = endereco
        self.senha = senha

    def validar_cpf(cpf):

        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        
        soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - (soma1 % 11)
        if digito1 >= 10:
            digito1 = 0

        soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = 11 - (soma2 % 11)
        if digito2 >= 10:
            digito2 = 0

        return cpf[-2:] == f"{digito1}{digito2}"

    def requisitar_endereco(self):
            self.req_endereco = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
            self.req_endereco = self.req_endereco.json()

            self.logradouro = self.req_endereco["logradouro"]
            self.bairro = self.req_endereco["bairro"]
            self.cep = self.req_endereco["cep"]
            self.cidade = self.req_endereco["localidade"]
            self.estado = self.req_endereco["uf"]
            
            self.endereco = (f"{self.logradouro}, {self.bairro}, {self.cidade} {self.estado}, CEP: {self.cep}")

            return self.endereco

    def inserir_nome(self):
        while True:
            self.nome = str(input("\nDigite o nome: "))
            nome_valido = self.nome.strip().replace(" ", "")

            if nome_valido.isalpha():
                return self.nome.upper()
            else:
                print("Existem caracteres inválidos ou o nome está em branco. Digite novamente!")
            
    def inserir_cpf(self):
        while True:
            self.cpf = str(input("Digite o CPF: "))
            if Jogador.validar_cpf(self.cpf):
                return self.cpf
            print("Digite um cpf válido!")
    
    def inserir_email(self):
        provedores_email = [
                            "@gmail.com", "@hotmail.com", "@outlook.com",
                            "@yahoo.com", "@icloud.com", "@mail.com",
                            "@uol.com.br", "@bol.com.br", "@ig.com.br"   
                            ]
        while True:
            self.email = str(input("Digite seu email: "))

            posicao_arroba = self.email.find("@")

            if self.email[posicao_arroba:] in provedores_email:
                return self.email.lower()
            print("Digite um email válido!")

    def inserir_idade(self):
        while True:
            self.idade = str(input("Digite sua idade: "))
            if self.idade.isdigit():
                return int(self.idade)
            print("Digite uma idade válida!")

    def inserir_senha(self):
        while True:
            self.senha = str(input("Digite a sua senha: "))
            self.senha_confirmacao = str(input("Digite novamente a senha: "))
            if self.senha == self.senha_confirmacao:
                confirma = str(input(f"Senha: {self.senha}. Confirma? [S/N]: ")).lower()
                if confirma == 's':
                    return self.senha
                else:
                    break
            else:
                print("As senhas não coincidem.")

    def inserir_cep(self):
        while True:
            self.cep = str(input("Digite o seu cep: "))
            self.cep = ''.join(filter(str.isdigit, self.cep))
            self.requisitar_endereco()

    def confirmar_insercao(self, nome):
        self.confirma = str(input(f"Deseja confirmar o cadastro do usuário {nome}? [S/N]: ")).lower()
        if self.confirma == 's':
            return True
        else:
            self.confirma2 = str(input("Deseja realmente cancelar o cadastro? [S/N]: ")).lower
            if self.confirma2 == 's':
                return False
            return True
        
    def buscar_cpf(self):
        #inicialização do banco de dados
            banco = sql.connect("jogo_forca.db")
            cursor = banco.cursor()
            cpf = self.cpf
            
            cursor.execute("SELECT * FROM jogador WHERE cpf = ?", (cpf,))
            resultado = cursor.fetchall()

            if resultado:
                print("Usuário já cadastrado.")
                banco.close()
                return False
            else:
                banco.close()
                return True

    def cadastrar_usuario(self):
        self.nome = self.inserir_nome()
        self.cpf = self.inserir_cpf()
        if self.buscar_cpf():
            self.email = self.inserir_email()
            self.idade = self.inserir_idade()
            self.endereco = self.inserir_cep()
            self.senha = self.inserir_senha()
            if self.confirmar_insercao(self.nome):
                #inicialização do banco de dados
                banco = sql.connect("jogo_forca.db")
                cursor = banco.cursor()
                #inserção dos dados de novo usuário
                cursor.execute("INSERT INTO jogador VALUES {self.nome, self.cpf, self.email, self.idade, self.endereco, self.senha}")
                #salvamento do banco de dados
                banco.commit()
                print("Usuário cadastrado com sucesso.")
                banco.close()
        return