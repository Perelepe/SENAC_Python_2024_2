def conceituar(media):
    if media>=9:
        conceito="O"
    elif (7<=media and media<=8.9):
        conceito="B"
    elif (5<=media and media<=6.9):
        conceito="S"
    else:
        conceito="I"
    return conceito

def main():
    x=float(input("Escreva a primeira nota: "))
    y=float(input("Escreva a segunda nota: "))

    media=(x+y)/2

    conceito=conceituar(media)
    
    print("Sua media é",media,"e seu conceito é",conceito +"!")

main()