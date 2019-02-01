listaNum = [[],[]]
num = 0
for c in range(1,8):
    num = int(input(f'Informe o {c}º valor: '))
    if num % 2 == 0:
        listaNum[0].append(num)
    else:
        listaNum[1].append(num)
listaNum[0].sort()
listaNum[1].sort()

print(listaNum[0])
print(listaNum[1])
