Num = int(input("Insira sua idade:"))
if Num <12 and Num >0:
    print("Você é uma criança.")
elif Num >12 and Num <17:
    print("Você é um adolescente.")
elif Num >18 and Num <59:
    print("Você é um adulto.")
elif Num >60:
    print("Você é um idoso.")
else:
    print("Idade invalida.")