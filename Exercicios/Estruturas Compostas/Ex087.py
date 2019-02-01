matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceiraColuna = maiorValor = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Informe o número da posição [{linha}][{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
        if matriz[1][coluna] > maiorValor:
            maiorValor = matriz[linha][coluna]
        if matriz[linha][2]:
            somaTerceiraColuna += matriz[linha][coluna]

#EXIBIR MATRIZ
print('-=' * 40)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end ='')
    print()
print(f'\nSoma dos valores pares: {somaPares}')
print(f'Soma dos valores da 3ª Coluna: {somaTerceiraColuna}')
print(f'Maior valor da segunda linha: {maiorValor}')