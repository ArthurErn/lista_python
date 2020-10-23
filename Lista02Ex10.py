print("Informe sua altura")
altura = float(input())
print("Informe seu Sexo (M/F)")
sexo = input()

if sexo == "M":
    altura = (72.7 * altura) - 58
elif sexo == "F":
    altura = (62.1 * altura) - 44.7
else:
    print("Informe o sexo corretamente")

print(f"Seu peso ideal é de {round(altura, 2)} KG")