
def CriarArquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "x")
        arquivo.close()
        print("==Arquivo criado com sucesso==")
    except FileExistsError:
        print("Esse arquivo já existe")
        arquivo = open(nome_arquivo, "r")
        arquivo.close()
nome_arq = "extensão.txt"
CriarArquivo(nome_arq)