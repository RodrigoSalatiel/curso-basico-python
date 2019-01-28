##TABOADA
num = int(input('Informe o número: '))
print('TABOADA DO {}'.format(num))
for c in range(1,11):
    print('{} x {} = {}'.format( c, num, c * num))
