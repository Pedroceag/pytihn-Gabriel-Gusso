#python
# importa o módulo random para seleção aleatório de palavras 
import random

# Lista de palavras para o jogoo (banco de palavras)
palavras - ['maça', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    """
    função principal que gerencia todo a lógica do jogo de forca:
    -Seleção da palavra 
    -Controle de tentativas 
    -Validação das letras 
    -Exibição do estado do jogo 
    """

    # Seleciona aleatóriamente uma palavra da lista 
    palavras_secreta = ramdom.choice(palavras)

    # Lista para armazenar as letras descubertas (iniciante todas ocultas)
    letras_corretas = ('_') * len(palavras_secreta)

    # Lista para registrar letras incorretas digitadas 
    letras_erradas = []

    # Define o número máximo de tentativas permitidas
    tentativas_restantes = 6

    # Mensagem inicial do jogo 
    print("\nbem-vindo ao jogo da força!")
    print(f"Você tem {tentativas_restantes}tentativas para adivinhar a palavra.\n")

    # Loop principal do jogo: continua enquanto houver tentativas e letras faltando 
    while tentativas_restantes > 0 and '_' in letras_corretas:
        # Exibe o progresso atual do jogador 
        print(' '. join (letras_corretas))

        