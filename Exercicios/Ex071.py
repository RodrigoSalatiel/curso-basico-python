print('=' * 40)
print('{:^40}'.format('BANCO DO SALA'))
print('=' * 40)
cedula = 100
valor = int(input('Digite o valor a ser sacado: R$ '))
total = valor
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de cédulas de R${cedula:.2f}: {totalCedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break