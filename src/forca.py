import speech_recognition as sr
from perguntas import Perguntas

def reconhecer_letra():
    
     # inicializa o reconhecedor de voz criando uma instancia de sua classe
    reconhecedor = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Ajustando para ruído de fundo. Aguarde um momento...")
        reconhecedor.adjust_for_ambient_noise(source, duration=3)
        
        print("Fale algo: ")
        
        try:
            # Chama a funcao de reducao de ruido disponivel na speech_recognition
            # reconhecedor.adjust_for_ambient_noise(source)
            
            # audio é um objeto que recebe uma informação de audio a partir do método listen()
            audio = reconhecedor.listen(source, timeout=4, phrase_time_limit=4)
            
            
             
            # conversão de audio em texto usando o serviço de reconhecimento de fala do google
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            
        # Retorna tudo que o jogador disser:
            return texto
        
        except sr.UnknownValueError:
            print("Não entendi o que você disse. Tente novamente.")
        except sr.RequestError as e:
            print(f"Erro no serviço de reconhecimento de fala: {e}")


def separar_letra(texto):
    texto = texto[0]
    if len(texto) == 1 and texto.isalpha():
     print(f"Você falou a letra: {texto.upper()}")
    else:
     print("Por favor, fale apenas uma letra.")
    
    
def jogo_forca():
    #cria uma instância da classe Perguntas
    dados_aleatorios = Perguntas()
    
    #chama o método para preencher os atributos das perguntas de forma aleatória
    dados_aleatorios.sortear_pergunta()
    
    palavra = dados_aleatorios.palavra
    dica = dados_aleatorios.dica
    max_tentativas = int(dados_aleatorios.max_tentativas)
    tentativas_restantes = int(max_tentativas)
    palavra_secreta = ['']*len[palavra]
    
    while True:
        
        texto = reconhecer_letra()
        letra = separar_letra(texto)
        
        mensagem = f'''
                ------------------ Jogo da Forca -----------------

                Dica:{dica}

                Palavra: {palavra_secreta})

                Tentativas: {tentativas_restantes} / {max_tentativas}

                    Fale uma letra:{letra}                          
        '''

        print(mensagem)
        
        if tentativas_restantes != 0:
            for letra_falada in letra:
                print(f'Tentando a letra: {letra_falada}')
                
                if letra_falada in palavra:
                    for i, letra_contida in enumerate(palavra):
                        if letra_contida == letra_falada:
                            palavra_secreta[i] = letra_falada
                else:
                    tentativas_restantes -= 1        
        else:
            print(f"\nVocê perdeu!\n")
            break       
    
