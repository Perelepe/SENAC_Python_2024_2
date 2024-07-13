#Programa que lê [nome], [endereço] e [telefone] de alguem e vai adicionando numa agenda

def spacer(tabela,chave):

    tamanho=0

    for i in range(len(tabela)):
        if (len(tabela[i][chave]))>tamanho:
            tamanho=len(tabela[i][chave])

    return tamanho+1

def criarAgenda():
    
    opcao=0
    agenda=[]

    while(opcao!=3):
        opcao=int(input("\nMenu:\n1-Incluir\n2-Listar\n3-Fim\n\nO que você deseja fazer? "))

        match opcao:

            case 1:
                nome=input("Qual o nome a inserir? ")
                endereco=input("Qual o endereço a inserir? ")
                telefone=input("Qual o telefone a inserir ( (xx) xxxxx-xxxx)? ")
                agenda.append({"nome":nome, "endereco":endereco, "telefone":telefone})

            case 2:
                maxNome=spacer(agenda,"nome")
                maxEndereco=spacer(agenda,"endereco")
                
                for i in range(len(agenda)):
                    espacoNome=(1+maxNome-len(agenda[i]["nome"]))*" "
                    espacoEndereco=(1+maxEndereco-len(agenda[i]["endereco"]))*" "
                    print("Nome:",agenda[i]["nome"]+espacoNome+"| Endereço:",agenda[i]["endereco"]+espacoEndereco+"| Telefone:",agenda[i]["telefone"])

            case 3:
                break

            case _:
                print("Entrada inválida.")
                continue

def main():
    criarAgenda()

main()