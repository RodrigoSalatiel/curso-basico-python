primeiro = int(input('Informe o 1º termo da PA: '))
razaoPA = int(input('Informe a razão da PA '))
termo = primeiro
contador = 0
ultimoTermo = 0
while contador < 10:
    print('{} '.format(termo), end =', ')
    termo += razaoPA
    contador += 1
