#FATORIAL
#UTILIZANDO O MÓDULO
'''from math import factorial
n = int(input('Informe um número para calcular seu fatorial: '))
f = factorial(n)
print('{}! = {}'.format(n, f))'''

#FAZENDO DO MODO TRADICIONAL, SEM UTILIZAR O MÓDULO
n = int(input('Informe o número: '))
contador = n
fatorial = 1
print('Calculando {}!...'.format(n))
while contador > 0:
    print('{}'.format(contador), end = '')
    print(' x ' if contador > 1 else ' = ', end = '')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))





