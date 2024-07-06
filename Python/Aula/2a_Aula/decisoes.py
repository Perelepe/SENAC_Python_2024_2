x=float(input("Digite o primeiro valor: "))
y=float(input("Digite o segundo valor: "))

if (x<y):
    print("y é maior que x")
elif (x>y):
    print("x é maior que y")
else:
    print("x e y são iguais")

if x<y or y<x:
    print("x e y são diferentes")
elif x==y and y==x:
    print("x e y são iguais")
else:
    print("como que tu fez essa proeza, querido?")