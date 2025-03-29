Num1 = int(input("Insira o primeiro numero: "))
Num2 = int(input("Insira o segundo numero: "))
Num3 = int(input("Insira o terceiro numero: "))

if Num1 > Num2 and Num1 > Num3:
    print(Num1, " é o maior numero.")
elif Num2 > Num1 and Num2 > Num3:
    print(Num2, " é o maior numero.")
elif Num3 > Num1 and Num3 > Num2:
    print(Num3, " é o maior numero.")
else:
    print("Numero invalido ou repetido.")