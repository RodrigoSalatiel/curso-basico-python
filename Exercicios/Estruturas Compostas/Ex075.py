numerosPares = ()
num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
if 9 in num:
    print(f'Quantidade de vezes que o número 9 aparece na Tupla: {num.count(9)}')
else:
    print('O valor 9 não foi encontrado!')
if 3 in num:
    print(f'Posição em que o número 3 foi digitado pela primeira vez: [{num.index(3)}]')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares digitados foram: ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end = '  ')