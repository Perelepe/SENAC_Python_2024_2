def exibirMensagem(): # Uma função sem parâmetros e sem retorno.
    print("Sou uma função!")

exibirMensagem()

def pedeNome(): # Uma função sem parâmetros e com retorno.
    nome=input("Qual o seu nome?\n")
    return nome


def exibirSaudacao(nome): # Uma função com parâmetros e sem retorno.
    print("Olá,", nome)

exibirSaudacao(pedeNome())