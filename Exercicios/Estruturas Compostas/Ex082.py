listaNum = list()
listaPares = list()
listaImpares = list()

while True:
    num = int(input('Digite um número: '))
    listaNum.append(num)
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)
    resp = str(input('Deseja continuar[S/N]? ')).lower()
    if resp == 'n':
        break
listaPares.sort()
listaImpares.sort()
listaNum.sort()
print(f'Lista de todos os números digitados: {listaNum}')
print(f'Lista apenas com os valores ímpares digitados: {listaImpares}')
print(f'Lista apenas com os valores pares digitados: {listaPares}')