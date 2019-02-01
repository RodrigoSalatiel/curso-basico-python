listaNum = list()
while True:
    num = int(input('Digite um número: '))
    listaNum.append(num)
    resp = str(input('Deseja continuar[s/n]? ')).lower()
    if resp == 'n':
        break

print(f'A) Quantidade de valores digitados: {len(listaNum)}')
listaNum.sort(reverse=True)
print(f'B) Lista exibida na ordem reversa: {listaNum}')
if 5 in listaNum:
    print('C) O valor 5 está presente na lista!')
else:
    print('C) O valor 5 não está presente na lista!')
