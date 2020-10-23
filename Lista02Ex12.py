print("Informe seu peso em KG")
peso = int(input())
print("Informe sua altura")
altura = float(input())

IMC = peso / (altura * 2)
print(f"Seu Indice de Massa Corporal é de {round(IMC, 2)}")

if IMC < 18.5:
    print("Você está abaixo do peso.")
elif IMC >= 18.5 and IMC < 25:
    print("Você está no peso normal.")
elif IMC > 25 and IMC <= 30:
    print("Você está acima do peso.")
else:
    print("Você está obeso")