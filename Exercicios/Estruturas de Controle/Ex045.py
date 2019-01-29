from random import choice

i = 0
while i <= 10:
    op = int(input('Informe o código desejado[1-3]: \n1 - Pedra \n2 - Papel \n3 - Tesoura \n'))
    listaOp = ['Pedra', 'Papel', 'Tesoura']
    adv = choice(listaOp)
    if op >=1 and op <=3:
        if op == 1:
            op = 'Pedra'.capitalize()
            print('')
            if op == adv:
                aux ='EMPATE'
            elif adv == 'Papel'.capitalize():
                aux = 'VOCÊ PERDEU!'
            else:
                aux = 'VOCÊ VENCEU!'
        if op == 2:
            op = 'Papel'.capitalize()
            print('')
            if op == adv:
                aux = 'EMPATE'
            elif adv == 'Tesoura'.capitalize():
                aux = 'VOCÊ PERDEU!'
            else:
                aux = 'VOCÊ VENCEU!'
        if op == 3:
            op = 'Tesoura'.capitalize()
            print('')
            if op == adv:
                aux = 'EMPATE'
            elif adv == 'Pedra'.capitalize():
                aux = 'VOCÊ PERDEU!'
            else:
                aux = 'VOCÊ VENCEU!'

        print('Escolha do jogador: {}'.format(op))
        print('Escolha do PC: {}'.format(adv))
        print('Resultado: {}'.format(aux))
    else:
        print('Informe uma opção válida!!')

