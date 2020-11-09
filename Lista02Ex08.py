num = []
num.append(int(input("Insira o primeiro valor")))
num.append(int(input("Insira o segundo valor")))
num.append(int(input("Insira o terceiro valor")))

if num[0] != num[1] and num[0] != num[2] and num[1] != num[2]:
    print(sorted(num, reverse=True))
else:
    print("Tente novamente")
    