distancia = int(input('Informe a distância da viagem em Km: '))
preco = 0
if distancia <= 200:
    preco = distancia * 0.5
    print('Distância: {} Km \nValor total da passagem: R${:.2f}'.format(distancia,preco))
else:
    preco = distancia * 0.45
    print('Distância: {} \nValor total da passagem: R${:.2f}'.format(distancia,preco))