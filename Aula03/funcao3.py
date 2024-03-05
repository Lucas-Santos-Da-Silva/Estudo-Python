def criaArquivo(nome="",ext="",cont="") -> str:
    """A funcao criaArquivo recebe o nome do arquivo a extensão e por fim algo para inserir no arquivo, e criar esse arquivo no diretotio local"""
    f= open(nome + "." + ext, "a")
    f.write(cont)
    f.close()
    return "Arquivo criado com sucesso"

print(criaArquivo("A janela","csv","texto;mensagem;ola"))