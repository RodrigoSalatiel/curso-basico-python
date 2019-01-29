import random

maiorValor = 0
menorValor = 0
aleatorio = (random.randint(0,999),random.randint(0,999), random.randint(0,999), random.randint(0,999), random.randint(0,999) )
print(f'Lista dos valores gerados: {aleatorio}')
cont = 0
while cont < 5:
    if cont == 0:
        maiorValor = aleatorio[0]
        menorValor = aleatorio[0]
    else:
        if aleatorio[cont] > maiorValor:
            maiorValor = aleatorio[cont]
        if aleatorio[cont] < menorValor:
            menorValor = aleatorio[cont]
    cont += 1
print(f'Maior valor gerado: {maiorValor}')
print(f'Menor valor gerado: {menorValor}')