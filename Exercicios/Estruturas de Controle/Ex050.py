##LER 6 NÚMEROS INTEIROS E SOMAR APENAS OS PARES
soma = 0
for c in range(1,7):
    num = int(input('Informe o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
print('Soma dos valores pares: {}'.format(soma))