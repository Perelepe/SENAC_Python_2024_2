def descobreEspecie(nome):
    match nome:
        case "Frodo" | "Sam":
            especie="Hobbit"
        case "Aragorn":
            especie="Homem"
        case "Gandalf":
            especie="Mago"
        case _:
            especie="Essa ai eu não conheço não"
    return especie

def main():
    nome=input("Informe o nome do personagem: ")
    
    especie=descobreEspecie(nome)
    
    print(especie)

main()
