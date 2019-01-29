num1 = float(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))
maiorNumero = 0
encerrar = False
while not encerrar:
    print('MENU \n[1]Somar \n[2]Multiplicar \n[3]Maior valor \n[4]Novos números \n[5]Sair')
    op = int(input('Informe a opcao desejada: '))
    if op !=5:
        if op == 1:
            print('Resultado = {} + {} = {}\n'.format(num1, num2, num1 + num2))
        if op == 2:
            print('Resultado = {} x {} = {}\n'.format(num1, num2, num1 * num2))
        if op == 3:
            if num1 > num2:
                maiorNumero = num1
            else:
                maiorNumero = num2
            print('Maior valor: {}\n'.format(maiorNumero))
        if op == 4:
            novoNum1 = float(input('Informe o 1º valor: '))
            novoNum2 = float(input('Informe o 2º valor: '))
            num1 = novoNum1
            num2 = novoNum2
    else:
        encerrar = True
print('CALCULADORA ENCERRADA!')



