from os import system
from time import sleep
from random import choice
from src.ler_arquivo import ler_arquivo_de_palavras
from unidecode import unidecode

# exibe as letras descobertas da palavras secreta
def exibir_palavra_secreta(palavra):
    for letra in palavra:
        print(letra, end=" ")

# cria uma pausa e depois limpa o terminal                     
def limpar_console():
    sleep(3)
    system("cls")
    
# executa o jogo    
def jogar():
    
    # cria uma lista com as palavras do arquivo de texto
    lista = ler_arquivo_de_palavras('./files/palavras.txt')

    # escolhe aleatoriamente uma das palavras da lista
    palavra_secreta = choice(lista)

    tentativas = 5

    # cria uma lista para exibir as letras descobertas da palavras secreta
    letras_da_palavra_secreta = ["_" for l in range(0, len(palavra_secreta))]
    
    # armazema os palpites de letras
    letras_ja_citadas = []
    
    while True:
        
        # encerra o jogo caso descubra todas as letras da palavra secreta
        if "".join(letras_da_palavra_secreta) == palavra_secreta:
            print(f'PARABENS, VOÇÊ ACERTOU TODAS AS LETRAS DA PALAVRA SECRETA {palavra_secreta.upper()}')
            break
        
        # encerra o jogo caso acabe as tentativas
        if tentativas == 0:
            print("FIM DE JOGO!")
            print(f'VOÇÊ NÃO ACERTOU Á PALAVRA SECRETA QUE ERA: {palavra_secreta.upper()}')
            break
        
        print(f'ACERTE A PALAVRA SECRETA')
        print(f"VOÇÊ TÊM {tentativas} TENTAVIVAS")
        exibir_palavra_secreta(letras_da_palavra_secreta)
        letra = input('\n> ').lower()

        # quebra o fluxo do jogo caso input não seja um único caractere   
        if len(letra) > 1:
            print("DIGITE APENAS UMA LETRA")
            limpar_console()
            continue
        
        # quebra o fluxo do jogo caso letra já tenha sido escolhida
        if letra in letras_ja_citadas:
            print("ESTA LETRA JÁ FOI ESCOLHIDA")
            limpar_console()
            continue
        
        # remove os acentos da palavra secreta para evitar problemas de verificação
        palavra_secreta_sem_acentos = unidecode(palavra_secreta)
        
        if letra in palavra_secreta_sem_acentos:
            
            # exibe mensagem caso a letra esteja na palavra secreta
            print('VOÇÊ ACERTOU UMA DAS LETRAS DA PALAVRA SECRETA')

            for i in range(0, len(palavra_secreta)):
                #caso encontre um hífem, armazena-o para exibir
                if palavra_secreta_sem_acentos[i] == "-":
                    letras_da_palavra_secreta[i] = palavra_secreta[i]
                
                # armazena a letra que foi acertada para ser exibida
                if letra == palavra_secreta_sem_acentos[i]:
                    letras_da_palavra_secreta[i] = palavra_secreta[i]
        else:
            # exibe mensagem caso a letra não esteja na palavra secreta
            print('QUE PENA, ESTA LETRA NÃO ESTÁ NA PALAVRA SECRETA')
            
            #diminui o números de tentativas
            tentativas -= 1   
           
        letras_ja_citadas.append(letra)       
        
        limpar_console()   
   
    