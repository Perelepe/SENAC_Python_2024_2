def exibirMensagem(): # Uma função sem parâmetros e sem retorno.
    print("Sou uma função!")

def pedeNome(): # Uma função sem parâmetros e com retorno.
    nome=input("Qual o seu nome?\n")
    return nome

def exibirSaudacao(nome, total): # Uma função com parâmetros e sem retorno.
    print("Olá,", nome)
    print("O total da soma é",total)

def somar(v1, v2):
    total=v1+v2
    return total

def main():
    exibirMensagem()
    soma=somar(6,9)
    print(soma)
    exibirSaudacao(pedeNome(),soma)

main()