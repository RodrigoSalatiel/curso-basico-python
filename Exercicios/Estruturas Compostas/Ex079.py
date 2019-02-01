listaNum = list()
while True:
    num = int(input('Digite um número: '))
    if num not in listaNum:
        listaNum.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já existente! Informe outro valor.')
    resp = str(input('Deseja continuar[s/n]? ')).lower()
    if resp == 'n':
        break
listaNum.sort()
print(f'Você digitou os valores: {listaNum}')