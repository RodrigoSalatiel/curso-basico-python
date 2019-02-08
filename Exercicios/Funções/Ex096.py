def area():
    largura = float(input('Informe a largura do terreno[m]: '))
    comprimento = float(input('Informe o comprimento do terreno[m]: '))
    area = largura * comprimento
    print(f'A área de um terreno {largura}m x {comprimento}m é de {area}m²')




#PROGRAMA PRINCIPAL
while True:
    area()
    while True:
        resp = str(input('Deseja continuar[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
            print('Opção inválida! Digite apenas "S" ou "N"')
    if resp == 'N':
        break
print('<<< PROGRAMA ENCERRADO! >>>')
