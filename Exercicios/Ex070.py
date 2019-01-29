precoTotal = acimaMilReais = 0
precoMaisBarato = 0
nomeMaisBarato = ''
cont = 1
while True:
    nomeProd = str(input('Informe o nome do produto: ')).title()
    precoProd = float(input('Informe o preço do produto: '))
    resp = str(input('Deseja adicionar mais produtos[s/n]? ')).lower()
    precoTotal += precoProd
    if cont == 1:
        precoMaisBarato = precoProd
        nomeMaisBarato = nomeProd
    else:
        if precoProd < precoMaisBarato:
            precoMaisBarato = precoProd
            nomeMaisBarato = nomeProd
    cont += 1
    if precoProd > 1000.00:
        acimaMilReais += 1
    if resp != 's':
        break
print('-=' * 40)
print(f'Valor total da compra: R${precoTotal:.2f} \nQuantidade de produtos acima de R$1000,00: {acimaMilReais}')
print(f'Nome do produto mais barato: {nomeMaisBarato}')