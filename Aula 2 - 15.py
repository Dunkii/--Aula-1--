Prod = input("Insira o produto desejado: ")
Price = float(input("Insira o valor do produto desejado: "))
Quant = int(input("Insira o numero de produtos desejados: "))

PricTot = Price * Quant
Desc  = PricTot * 0.05

if PricTot > 100:
    print("O valor a ser pago é ", PricTot - Desc, "R$")
else:
    print("O valor a ser pago é ", PricTot, "R$")