def isEven(n):
    return (n%2)==0

def main():
    n=int(input("Diga-me um número e te direis se é par!\n"))
    
    if isEven(n):
        paridade="é Par!"
    else:
        paridade="é Ímpar!"
        
    print(n,paridade)
main()