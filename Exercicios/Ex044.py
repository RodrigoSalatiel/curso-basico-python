preco = float(input('Informe o preço do produto: R$ '))
cod = int(input('Informe a opção de pagamento [1-4]: \n1 - À vista Dinheiro/Cheque \n2 - À vista no Cartão '
                '\n3 - Em até 2x no Cartão \n4 - 3x ou mais no cartão \nOpção: ' ))
formaDePagto = str
novoValor = 0


print('')
if cod >= 1 and cod <= 4:
    print('Preço padrão: R$ {:.2f}'.format(preco))
    if cod == 1:
        novoValor = preco * 0.9
        formaDePagto = 'À Vista em dinheiro/cheque'
    elif cod == 2:
        novoValor = preco * 0.95
        formaDePagto = 'À vista no Cartão de débito/crédito'
    elif cod == 3:
        novoValor = preco
        formaDePagto = '2x no cartão de crédito'
    elif cod == 4:
        novoValor = preco * 1.20
        formaDePagto = '3x ou mais no cartão de crédito'
    print('Opção: {}'.format(formaDePagto))
    print('Preço atualizado:  R$ {:.2f}'.format(novoValor))
else:
    print('Opção inválida, digite novamente!')



