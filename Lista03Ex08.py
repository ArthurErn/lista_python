chico = float(1.50)
ze = float(1.10)

for i in range(0, 50):
    chico = float(chico + 0.02)
    ze = float(ze + 0.03)
    if ze > chico:
        print(f"Foram necessários {i} anos para que Zé ficasse maior que Chico")
        break