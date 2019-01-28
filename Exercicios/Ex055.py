menorPeso = 0
maiorPeso = 0

for c in range(1,6):
    peso = float(input('Informe o peso do {}º paciente: '.format(c)))
    ##definir o maior e o menor peso para a 1º ocorrência do for
    if c == 1:
        menorPeso = peso
        maiorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('Maior Peso: {} kg \nMenor Peso: {} kg'.format(maiorPeso,menorPeso))