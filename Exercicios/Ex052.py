##NÚMEROS PRIMOS
totDiv = 0
aux =''
num = int(input('Informe o numero: '))
for c in range(1,num+1):
    if num % c == 0:
        totDiv += 1
        if totDiv == 2:
            aux = 'É PRIMO!'
        else:
            aux = 'NÃO É PRIMO'
print('O número {} {} '.format(num, aux))
