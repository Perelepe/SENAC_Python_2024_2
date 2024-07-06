nome = input("Qual é o seu primeiro nome?\n")
nome = nome.strip() #Remove os espaços antes e depois da string.
nome = nome.capitalize() #Muda o primeiro caracter de uma string para maíusculo e o resto para minúsculo, se possível.
if (' ' in nome):
    nome=nome.title() #Funciona como o capitalize, mas para cada uma das palavras
    primeiro, sobrenome = nome.split(" ") #Separa a string em x pedaços (baseado na quantidade de variaveis) pelo caracter dentro da função (" ").
    print("Olá,", primeiro, sobrenome, end=".\n")
    print(f"Não me lembro de ter pedido mais de um nome.")
else:
    print("Olá,", nome, end=".\n")
    print(f"Que coincidência, eu conheço outro {nome}.")


