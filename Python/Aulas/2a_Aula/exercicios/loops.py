def main():    
    n=int(input("Quantos gatos você tem?"))

    for i in range(0,n):
        print("Miau "+str(i+1))
    
    n=int(input("Quantos sapos você tem?"))

    for _ in range(n):
        print("Ribbit!")

    n=int(input("Quantos cachorros você tem?"))

    while n!=0:
        print("Auau "+str(n))
        n-=1
    
    print("\nFABIANO!!"*10, end="")
main()