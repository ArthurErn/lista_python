valorX = int(input("Informe o valor de X \n"))
valorY = int(input("Informe o valor de Y \n"))
valorZ = int(input("Informe o valor de Z \n"))
XZ = valorX + valorZ
XY = valorY + valorX
ZY = valorY + valorZ

if valorX >= ZY or valorZ >= XY or valorY >= XZ:
    print("As propriedades não correspondem")

else:
    if valorX == valorY and valorZ == valorX:
        print("Temos um triângulo equilátero")
    elif valorX != valorZ and valorX == valorY or valorZ != valorX and valorZ == valorY or valorY != valorZ and valorY == valorX:
        print("Temos um triângulo isósceles")
    else:
        print("Temos um triângulo escaleno")