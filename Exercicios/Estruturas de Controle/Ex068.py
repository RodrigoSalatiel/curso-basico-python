##PAR OU IMPAR
from random import randint
contVitorias = 0

while True:
    aux = ''
    computador = randint(0, 5)
    valor = int(input('Informe um valor entre 0 e 5: '))
    escolha = int(input('[1] Par \n[2]Ímpar \nQual a sua escolha?  '))
    if (valor + computador) % 2 == 0:
        aux = 'PAR'
    else:
        aux = 'ÍMPAR'
    print('-' * 30)
    print(f'Você jogou {valor} e o computador {computador}. Total de {valor + computador} que é {aux}')
    if escolha == 1:
        if (valor + computador) % 2 == 0:
            contVitorias += 1
            print('-' * 30)
            print('VOCÊ VENCEU!!!')
            print('-' * 30)
        else:
            break
    if escolha == 2:
        if(valor + computador) % 2 != 0:
            contVitorias += 1
            print('-' * 30)
            print('VOCÊ VENCEU!!!')
            print('-' * 30)
        else:
            break
print('-' * 40)
print(f'VOCÊ PERDEU! \nGAME OVER!! \nTotal de Vitórias Consecutivas: {contVitorias}')