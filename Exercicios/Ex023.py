numero = str(input('Informe um numero[0-9999]: ')).zfill(4)
print ('Número: {} \nUnidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(numero, numero[3],numero[2],numero[1], numero[0]))
