[![serra-horizontal-cor.jpg](https://i.postimg.cc/FK9R13nG/serra-horizontal-cor.jpg)](https://postimg.cc/cvbZbgW8)

# PROJETO FORCA

## Autores

- [Kauã Amorim](https://github.com/Kauanqualquercoisa)

- [Rômulo Santana](https://github.com/romulossant)

- [Amanda Frasson]()

## Email do Projeto

- jogoforca.poobj@gmail.com

## Descrição

Este projeto consiste na implementação de um jogo da forca desenvolvido em Python, com persistência de dados em um banco de dados SQLite. O sistema oferece diferentes funcionalidades para jogadores e administradores, incluindo cadastro, login, recuperação de senha e gerenciamento de perguntas.

## Funcionalidades

### **Menu principal:**

- Jogar
- Cadastrar novo jogador
- Recuperar senha
- Entrar como administrador
- Sair

### **Modo administrador:**

- Cadastrar, atualizar, remover e listar perguntas do banco de dados.

- Exportar perguntas para um arquivo CSV.

### **Modo jogador:**

- Sorteio aleatório de perguntas.
- Interação via voz para entrada de letras.
- Atualização de dados do jogador.
- Verificação de vitória ou término do jogo com base nas tentativas.

### **Recursos adicionais:**

- Consulta automática de endereço via API de CEP.

- Envio de senha gerada automaticamente via e-mail, utilizando o serviço do Gmail.

## Tecnologias utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![SQLite](https://img.shields.io/badge/SQLite-000?style=for-the-badge&logo=sqlite&logoColor=07405E)

## Bibliotecas

![Bagde](https://img.shields.io/badge/SpeechRecognition-para%20entrada%20de%20voz-purple)

![Bagde](https://img.shields.io/badge/Pyttsx3-para%20sintese%20de%20voz-purple)

![Bagde](https://img.shields.io/badge/Requests-para%20consumo%20da%20API%20de%20CEP-purple)

![Bagde](https://img.shields.io/badge/Smtplib-para%20envio%20de%20emails-purple)

## Como executar o projeto

### Requisitos

1.  **Certifique-se de ter o Python 3.6 ou superior instalado.**

2.  **Instale as bibliotecas necessárias:**

```bash
pip install SpeechRecognition pyttsx3 pipwin requests

pip install pyaudio
```

### Execução

1. Certifique-se de que todas as dependências estão instaladas.

2. Execute o arquivo principal do projeto:

```
python main.py
```

## Propriedades

- Uso de conceitos de Programação Orientada a Objetos (POO).

- Persistência de dados com SQLite.

- Interface amigável e simples.
