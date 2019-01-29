soma = totalNum = 0

while True:
    numero = int(input('Digite um número[999 para encerrar]: '))
    if numero == 999:
        break
    soma += numero
    totalNum += 1
print('-' * 40)
print(f'Total de números digitados: {totalNum} \nSoma dos números digitados: {soma}')