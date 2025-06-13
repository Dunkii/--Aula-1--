SalB = int(input("Insira o seu salario: "))
Horas = int(input("Insira o numero de horas extras: "))
ValExt = int(input("Insira o valor de cada hora extra trabalhada: "))

ValHor = Horas * ValExt
SalTot = SalB + ValHor

print("Seu salario a receber será de :", SalTot, "R$")
