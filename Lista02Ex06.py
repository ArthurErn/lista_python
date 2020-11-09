num = bool(input("Informe um valor: "))
num2 = bool(input("Informe outro valor: "))
if num == 1 and num2 == 1:
    print("VERDADEIRO")
elif num == 0 or num2 == 0:
    print("FALSO")
else:
    print("Por favor digite um número entre 1 ou 0")