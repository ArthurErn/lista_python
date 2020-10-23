print("Informe seu peso em KG")
peso = int(input())
print("Informe sua altura")
altura = float(input())

IMC = peso / (altura * 2)
print(f"Seu Indice de Massa Corporal é de {round(IMC, 2)}")
