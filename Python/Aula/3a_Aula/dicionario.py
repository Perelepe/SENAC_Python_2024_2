tabelaPersonagens = [
                    {
                        "nome":"Frodo", 
                        "especie":"Hobbit",
                        "local":"Condado"
                    },
                    {
                        "nome":"Sam",
                        "especie":"Hobbit",
                        "local":"Condado"
                    },
                    {
                        "nome":"Legolas",
                        "especie":"Elfo",
                        "local":"Valfenda"
                    },
                    {
                        "nome":"Aragorn",
                        "especie":"Homem",
                        "local":"Desconhecido"
                    },
                    {
                        "nome":"Gandalf",
                        "especie":"Mago",
                        "local":"Isengard"
                    },
                    {
                        "nome":"Gimli",
                        "especie":"Anão",
                        "local":"Desconhecido"
                    },
                    {
                        "nome":"Smeagol",
                        "especie":"Hobbit",
                        "local":"Desconhecido"
                    },
                    {
                        "nome":"Bilbo",
                        "especie":"Hobbit",
                        "local":"Desconhecido"
                    }
                    ]


dicioPersonagens = { #Pode escrever um ao lado do outro, mas assim fica melhor
                    "Frodo":"Hobbit", 
                    "Sam":"Hobbit", 
                    "Legolas":"Elfo", 
                    "Aragorn":"Homem", 
                    "Gandalf":"Mago", 
                    "Gimli":"Anão", 
                    "Smeagol":"Hobbit", 
                    "Bilbo":"Hobbit"
                   }
def spacer(tabela,chave):
    tamanho=0
    for i in range(len(tabela)):
        if (len(tabela[i][chave]))>tamanho:
            tamanho=len(tabela[i][chave])
    return tamanho+1

maxNome = spacer(tabelaPersonagens,"nome")
maxEspecie = spacer(tabelaPersonagens,"especie")

#ginly= motanha da perdicao
#gandalf=terra media
for indice in range(len(tabelaPersonagens)):
    espacoNome=(1+maxNome-len(tabelaPersonagens[indice]["nome"]))*" "
    espacoEspecie=(1+maxEspecie-len(tabelaPersonagens[indice]["especie"]))*" "
    print("Nome:",tabelaPersonagens[indice]["nome"]+espacoNome+"| Espécie:",tabelaPersonagens[indice]["especie"]+espacoEspecie+"| Local:",tabelaPersonagens[indice]["local"])


    