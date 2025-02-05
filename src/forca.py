import speech_recognition as sr
from perguntas import Perguntas
from unidecode import unidecode  # biblioteca para retirar os acentos
# biblioteca para colorir a mensagem no terminal
from colorama import Fore, Style, init

init()  # Inicializa o colorama


def reconhecer_letra():

    # inicializa o reconhecedor de voz criando uma instancia de sua classe
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nAjustando para ruído de fundo. Aguarde um momento...\n")
        while True:

            reconhecedor.adjust_for_ambient_noise(source, duration=3)

            print("\nFale algo: \n")
            try:
                # Chama a funcao de reducao de ruido disponivel na speech_recognition
                # reconhecedor.adjust_for_ambient_noise(source)

                # audio é um objeto que recebe uma informação de audio a partir do método listen()
                audio = reconhecedor.listen(
                    source, timeout=4, phrase_time_limit=4)

                # conversão de audio em texto usando o serviço de reconhecimento de fala do google
                texto = reconhecedor.recognize_google(audio, language='pt-BR')

            # Retorna tudo que o jogador disser:

                return texto

            except sr.UnknownValueError:
                print("\nNão entendi o que você disse. Tente novamente.\n")
                pass
            except sr.RequestError as e:
                print(f"\nErro no serviço de reconhecimento de fala: {e}\n")
                pass


def separar_letra(texto):

    texto = texto[0]
    if len(texto) == 1 and texto.isalpha():
        # print(f"Você falou a letra: {unidecode(texto.lower())}")
        return texto


def jogo_forca():
    # cria uma instância da classe Perguntas
    dados_aleatorios = Perguntas()

    # chama o método para preencher os atributos das perguntas de forma aleatória
    dados_aleatorios.sortear_pergunta()

    palavra = unidecode(dados_aleatorios.palavra.lower())
    palavra = palavra.replace(" ", "_")
    dica = dados_aleatorios.dica
    max_tentativas = int(dados_aleatorios.max_tentativas)
    tentativas_restantes = int(max_tentativas)
    palavra_secreta = ['_']*len(palavra)

    while True:

        mensagem = f'''
                ------------------ Jogo da Forca -----------------

                Dica:{dica}

                Palavra: {''.join(palavra_secreta)}

                Tentativas: {tentativas_restantes} / {max_tentativas}

                    Fale uma letra:
        '''

        print(mensagem)

        texto = reconhecer_letra()
        letra = unidecode(separar_letra(texto).lower())

        if tentativas_restantes != 0:
            for letra_falada in letra:
                print(f'Tentando a letra: {letra_falada}')

                if letra_falada in palavra:
                    for i, letra_contida in enumerate(palavra):
                        if letra_contida == letra_falada:
                            palavra_secreta[i] = letra_falada
                else:
                    tentativas_restantes -= 1

            if ''.join(palavra_secreta) == palavra:

                palavra = palavra.replace("_", " ")

                mensagem = f'''
                ------------------ Jogo da Forca -----------------

                Dica:{dica}

                Palavra: {palavra}

                Tentativas: {tentativas_restantes} / {max_tentativas}


                '''

                print(mensagem)

                print(Fore.GREEN + "\nParabéns, você ganhou!\n" + Style.RESET_ALL)
                break

        else:
            print(Fore.RED + "\nVocê perdeu!\n" + Style.RESET_ALL)
            break
