#SOMA DE TODOS OS NUMEROS IMPARES ENTRE 1 E 500

soma = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print('O somátorio dos números ímpares e multiplos de 3 entre 1 e 500 é {}'.format(soma))

