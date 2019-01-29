dinheiro = float(input('Informe a quantidade de dinheiro disponível para câmbio: '))
vlDolar = 3.27
print('Total em R$: {:.2f} \nTaxa de câmbio do US$: {} \nTotal em US$: {:.2f}'.format(dinheiro, vlDolar, dinheiro/vlDolar))