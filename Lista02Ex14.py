aluno = input("Digite o número de identificação do aluno\n")
ME = int(input("Informe a média nos exercícios do aluno \n"))
nota1 = int(input("Informe a primeira nota da prova \n"))
nota2 = int(input("Informe a segunda nota da prova \n"))
nota3 = int(input("Informe a terceira nota da prova \n"))

if nota1 < 0 or nota2 < 0 or nota3 < 0 or ME < 0:
    print("Por favor, informe as notas corretamente")
else:
    MA = (nota1 + nota2 * 2 + nota3 * 3 + ME) / 7
    print(f"A média do aluno de código {aluno} é {round(MA, 2)}")