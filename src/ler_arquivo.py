# realiza a leitura do arquivo e retorna em uma lista
def ler_arquivo_de_palavras(arquivo):
    
    with open(arquivo, 'r') as txt:
        lista_de_palavras = txt.readlines()
        
        for p in range(0, len(lista_de_palavras)):
            #remove quebra de linhas em cada item da lista
            lista_de_palavras[p] = lista_de_palavras[p].rstrip()
            
    return lista_de_palavras           