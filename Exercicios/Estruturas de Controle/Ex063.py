print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
n = int(input('Informe quantos termos deseja mostrar: '))
termo1 = 0
termo2 = 1
res = 0
contador = 1
print('~' * 30)
print('{} → {} → '.format(termo1,termo2), end = '')
while contador < n - 1:
    res = termo1 + termo2
    termo1 = termo2
    termo2 = res
    contador += 1
    print('{} → '.format(res), end = '' )
print('FIM')