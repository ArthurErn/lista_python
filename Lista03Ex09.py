aux = int(input("Digite um numero positivo, ou <= 0 para parar"))
menor = aux
maior = aux
while True:
    aux = int(input("Digite um numero positivo, ou <= 0 para parar"))
    if aux > maior:
        maior = aux
    if aux <= menor and aux > 0:
        menor = aux
    if aux == 0:
        break
print(f'O maior número é {maior}, e o menor {menor}')
        