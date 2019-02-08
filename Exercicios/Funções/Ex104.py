def leiaInt(msg = ''):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('ERRO! Digite um número inteiro válido!')
    return valor


#PROGRAMA PRINCIPAL
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')