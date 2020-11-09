valorA = float(input("Informe o valor de A "))
valorB = float(input("Informe o valor de B "))

if valorA == valorB:
    valorC = valorA + valorB
    print(f'O valor de C vale: {valorC:.2f}')
else:
    valorC = valorA * valorB
    print(f'O valor de C vale: {valorC:.2f}')