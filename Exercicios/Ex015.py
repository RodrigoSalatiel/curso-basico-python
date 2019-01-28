diasAlugados = int(input('Informe a quantidade de dias que o veículo ficou alugado: '))
kmRodados = float(input('Informe quantos Km o veículo percorreu neste período: '))
totalValorDias = diasAlugados * 60
totalKmRodados = kmRodados * 0.15
totalAPagar = totalValorDias + totalKmRodados
print('Quantidade de dias de aluguel: {} dias \nQuantidade de Km percorridos: {:.0f}Km \nTotal a pagar: R${:.2f}'
      .format(diasAlugados, kmRodados, totalAPagar))