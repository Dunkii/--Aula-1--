Escolha = str(input('Adicione um item na sacola: '))
Compras = Escolha
while True:
    escolha2 = str(input('deseja adicionar outros itens? Sim ou Não: '))
    if escolha2 == 'Não':
        break
    else:
        Compras.append(Escolha)
print(f'Os itens da lista de compras são: {Compras}')