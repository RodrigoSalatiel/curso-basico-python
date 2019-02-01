listaNum = list()
for c in range(0,5):
    num = int(input(f'Digite o {c + 1} valor: '))
    if c == 0 or num > listaNum[-1]:
        listaNum.append(num)
        print('Adicionado ao final da lista! ')
    else:
        pos = 0
        while pos < len(listaNum):
            if num<= listaNum[pos]:
                listaNum.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista! ')
                break
            pos +=1
print('-' * 40)
print(f'Os valores digitados em ordem foram: {listaNum}')