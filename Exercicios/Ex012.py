preco = float(input('Informe o Preço do produto: '))
desc = int(input('Informe o valor do desconto: '))
print('Preço: R${:.2f} \nPreço com {:.2f}% de desconto: R${:.2f}'.format(preco, desc, (100 - desc)/100 * preco))