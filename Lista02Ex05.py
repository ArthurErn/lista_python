numero = float(input("Informe o número: "))

if numero > 0:
    numero = numero * 2
    print(f'O valor é {numero:.2f}')
elif numero < 0:
    numero = numero * 3
    print(f'O valor é {numero:.2f}')
else:
    print("Por favor digite um valor diferente de 0")