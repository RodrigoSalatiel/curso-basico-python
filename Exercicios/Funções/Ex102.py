def fatorial(num, show = False):
    """
    -> Calcular o fatorial de um número
    :param num: Valor a ser calculado o fatorial
    :param show(Opcional): Se deseja ou não exibir o processo de cálculo
    :return: O valor do fatorial
    """
    fatorial = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        fatorial *= c
    return fatorial


# PROGRAMA PRINCIPAL
num = int(input('Digite um número para calcular o fatorial: '))
bol = False

while True:
    show = str(input('Deseja mostrar o processo de cálculo[S/N]? ')).upper()[0]
    if show in 'SN':
        break
    print('Valor invpalido. Digite apenas "S" ou "N')
if show == 'N':
    bol = False
else:
    bol = True
print(f'{num}! = ', end = '')
print(f'{fatorial(num, bol)}')