numero = float(input("Digite um número: "))

if numero % 2 == 0:
    numero = numero + 5
    print(f"Valor: {numero:.2f}")
else:
    numero = numero + 8
    print(f"Valor: {numero:.2f}")