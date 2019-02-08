from time import sleep

def contador(inicio, fim, passo):
    print('-' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end = '', flush= True)
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end = '', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print('Agora é a sua vez de personalizar o contador!!')
inicio = int(input('Informe o inicio do contador: '))
fim = int(input('Informe o final do contador: '))
passo = abs(int(input('Informe o passo do contador: ')))
contador(inicio, fim, passo)
