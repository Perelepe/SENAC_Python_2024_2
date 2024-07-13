# Exceptions
# try
# except
erro=True
while(erro):
    try :
        x = int(input("Digite o valor de x: "))
    except ValueError:
        print("Por favor, insira um inteiro.")
        continue
    erro=False

while(1):
    try :
        y = int(input("Digite o valor de y: "))
    except ValueError:
        print("Por favor, insira um inteiro.")
        continue
    else:
        break

print(f"x é {x}")

print("y é %d" % (y))
