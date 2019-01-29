velocidade = int(input('Digite a velocidade em que o veículo passou no radar: '))
if velocidade <= 80:
    print('Parabéns, você é um motorista consciente e respeita as leis de trânsito!')
    print('Velocidade no radar: {} km/h'.format(velocidade))
else:
    totalMulta = (velocidade - 80) * 7
    print('MULTADO! Na próxima vez ande dentro dos limites de velocidade')
    print('Velocidade no radar: {} km/h \nValor da multa: R${:.2f} \nKm acima do permitido: {} km/h'.format(velocidade, totalMulta, velocidade-80))
