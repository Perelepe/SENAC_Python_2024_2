def descobreEspecie(nome, especies):
    match nome:
        case "Frodo" | "Sam" | "Bilbo" | "Smeagol":
            i=0
        case "Aragorn":
            i=1
        case "Gandalf":
            i=2
        case "Ginly":
            i=3
        case "Legolas":
            i=4
        case _:
            i=-1
    return especies[i]

personagens=["Frodo", "Sam", "Legolas", "Aragorn", "Gandalf", "Ginly", "Smeagol", "Bilbo"]

especies=["Hobbit", "Homem", "Mago", "Anão", "Elfo", "Desconhecida"]

i=0

print("Personagens:")
print(personagens)
print("Espécies:")
print(especies)

for personagem in personagens:
    especie=descobreEspecie(personagem, especies)
    espacos=(1+len(max(personagens))-len(personagem))*" "
    print("Nome:", personagem+espacos+"|"+" Espécie:", especie)

#for i in range(len(personagens)):
#    print("Nome: ", personagem[i], "Espécie: ", especies[i])