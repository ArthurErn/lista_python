print("Insira o valor de A")
A = int(input())
print("Insira o valor de B")
B = int(input())
print("Insira o valor de C")
C = int(input())
print("Insira o valor de D")
D = int(input())
menor = A
maior = A

if B > maior:
    maior = B
if C > maior:
    maior = C
if D > maior:
    maior = D

if B < menor:
    menor = B
if C < menor:
    menor = C
if D < menor:
    menor = D

print(f"O maior valor é {maior}")
print("=================")
print(f"O menor valor é {menor}")