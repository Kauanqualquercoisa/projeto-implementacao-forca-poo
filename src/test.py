import speech_recognition as sr


def reconhecer_audio():
    
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
            
            with open("teste_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
             
            # conversão de audio em texto usando o serviço de reconhecimento de fala do google
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            
        # Verifica se é uma única letra
            print(texto)
            #if len(texto) == 1 and texto.isalpha():
              #  print(f"Você falou a letra: {texto.upper()}")
            #else:
              #  print("Por favor, fale apenas uma letra.")
        except sr.UnknownValueError:
            print("Não entendi o que você disse. Tente novamente.")
        except sr.RequestError as e:
            print(f"Erro no serviço de reconhecimento de fala: {e}")

if __name__ == "__main__":
    reconhecer_audio()

