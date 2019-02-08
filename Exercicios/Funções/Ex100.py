from random import randint
from time import sleep

def sorteia():
    print('Sorteando 5 valores da lista: [', end='')
    for num in range(0,5):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num}    ', end='', flush=True)
        sleep(0.5)
    print('] PRONTO!')
    return numeros


def somaPar(num):
    somaPar = 0
    print(f'A soma dos valores PARES de [', end = '')
    for v in num:
        print(f'{v}    ', end = '', flush=True)
        sleep(0.5)
        if v % 2 == 0:
            somaPar += v
    print(f'] é igual a {somaPar}')

def somaImpar(num):
    somaImpar = 0
    print('A soma dos valores ÍMPARES de [', end = '')
    for v in num:
        print(f'{v}   ', end='', flush=True)
        sleep(0.5)
        if v % 2 != 0:
            somaImpar += v
    print(f'] é igual {somaImpar} ')


#PROGRAMA PRINCIPAL
numeros = list()
sorteia()
somaPar(numeros)
somaImpar(numeros)