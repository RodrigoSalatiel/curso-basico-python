'''Utilizando for
for c in (1,10)
    print(c)
print('Fim')'''

#Utilizando WHILE para executar os comandos acima
'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''

qtdPar = 0
qtdImpar = 0
totNum = 0
n = 1
while n != 0:
    n = int(input('digite o número: '))
    if n != 0:
        totNum += 1
        if n % 2 == 0:
            qtdPar += 1
        else:
            qtdImpar += 1
print('Programa Encerrado! \nTotal de valores digitados: {} \nTotal de valores pares: {} \nTotal de valores ímpares: {}'.format(totNum,qtdPar,qtdImpar))

