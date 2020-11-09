numero = int(input('Digite um número:\n'))
total = 0
i = 0

if numero > 0:
    while True:
        i += 1
        total = total + i
        if total == numero:
            print('O número é perfeito')
            break
else:
    print("Por favor digite um número positivo")
