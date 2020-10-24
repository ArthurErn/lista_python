maior = 0

for i in range(0, 15):
    aux = int(input("Digite um número: "))
    if i == 0:
        menor = aux
        maior = aux
    if aux > maior:
        maior = aux
    if menor > aux:
        menor = aux
    
print(f"O maior valor é {maior}, e o menor {menor}")
    
    
