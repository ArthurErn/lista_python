soma = 0

while True:
    auxiliar = float(input("Digite um número para adicionar a soma e '0' para parar\n"))
    if auxiliar == 0:
        break
    soma = soma + auxiliar
print(f'A soma deu {soma:.2f}')
