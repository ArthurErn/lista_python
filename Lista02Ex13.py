print("Quanto deve ser pago pelo produto?")
preco = float(input())
print("Em quantas vezes? (1/2)")
vezes = int(input())
print("Modo de pagamento | 1 - Dinheiro | 2 - Cheque | 3 - Cartão")
modo = int(input())

if vezes == 1:
    if modo == 1 or modo == 2:
        total = (preco * 0.10)
        print(f"O seu desconto é de R${int(total)}")
    elif modo == 3:
        total = (preco * 0.15)
        print(f"O seu desconto é de R${int(total)}")
    else:
        print("Modo de pagamento inválido")

elif vezes == 2:
    if modo > 3:
        print("Modo de pagamento inválido")
    elif modo > 0 and modo <= 2:
        print("1 - Sem juros | 2 - Com juros")
        juros = int(input())
        if juros == 1:
            print(f"Preço normal de R${preco}")
        elif juros == 2:
            total = preco + (preco * 0.10)
            print(f"Preço com 10% de juros, preço total de R${total}")
        else:
            print("Número inválido")
elif vezes > 2:
    print("Número de vezes inválido")
