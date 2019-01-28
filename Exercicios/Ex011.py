larg = float(input('Informe a Largura da parede: '))
alt = float(input('Informe a Altura da parede: '))
area = larg * alt
print('Área da parede: {:.2f}m \nQuantidade de tinta necessária: {:.2f}L'.format(area, area/2))