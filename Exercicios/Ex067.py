print('-' * 40)
print('TABUADA FÁCIL')
print('-' * 40)

while True:
    numero = int(input('Você deseja saber a taboada de qual número? '))
    if numero > 0:
        multiplicador = 1
        resultado = 0
        while multiplicador <= 10:
            resultado = numero * multiplicador
            print(f'{numero} x {multiplicador} = {resultado}')
            multiplicador += 1

    else:
        break
print('Valores negativos não são aceitos. Programa Encerrado!')