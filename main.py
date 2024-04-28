from src.game import jogar, limpar_console

if __name__ == "__main__":

    jogar()
    limpar_console()
    
    while True:
        print("VOÇÊ QUER JOGAR NOVAMENTE?\n(digite 's' para confirmar ou pressione qualquer tecla para sair)")
        tecla = input('> ')
    
        if tecla == 's':
            limpar_console()
            jogar()
            limpar_console()
        else:
            break 
