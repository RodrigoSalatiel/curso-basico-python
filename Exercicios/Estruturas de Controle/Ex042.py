segA = float(input('Informe a medida do Segmento A: '))
segB = float(input('Informe a medida do Segmento B: '))
segC = float(input('Informe a medida do Segmento C: '))

print('\n')
if segA<segB+segC and segB<segA+segC and segC<segA+segB and segA>abs(segB-segC) and segB>abs(segA-segC) and segC>abs(segA-segB):
    print('As medidas PODEM formar um Triângulo!!')
    if segA == segB == segC:
        print('Tipo do Triângulo: EQUILÁTERO')
    elif segA != segB != segC:
        print('Tipo do Triângulo: ESCALENO')
    else:
        print('Tipo do Triângulo: Isósceles')
else:
    print('As medidas NÃO PODEM formar um triângulo!!')