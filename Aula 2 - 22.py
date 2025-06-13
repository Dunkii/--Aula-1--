verificacao = 0
senha = 'Nick'
usuario = '12345'
for tentativa in range(3):
    usuario = str(input('Digite o usuário: '))
    senha = str(input('Digite a senha: '))
    if usuario == 'Nick' and senha == '12345':
        verificacao = 1
        break
    else:
        print('Usuário ou senha errados, tente novamente')
if verificacao == 1:
    print('Acesso autorizado!')
else:
    print('Acesso negado!')