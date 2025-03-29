Num1 = int(input("Insira o primeiro valor: "))
Num2 = int(input("Insira o segundo valor: "))
Op = input("Selecione a operação desejada: ")

if Op == "+":
    Solve = Num1 + Num2
    print(Solve)
elif Op == "-":
    Solve = Num1 - Num2
    print(Solve)
elif Op == "*":
    Solve = Num1 * Num2
    print(Solve)
elif Op == "/":
    Solve = Num1 / Num2
    print(Solve)
else:
    print("A operação não existe.")