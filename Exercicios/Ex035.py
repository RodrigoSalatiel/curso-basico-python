import math

print('==== VERIFICAR CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO ====')
segA = float(input('Informe a medida do segmento A: '))
segB = float(input('Informe a medida do segmento B: '))
segC = float(input('Informe a medida do segmento C: '))
msgY = 'Os segmentos acima PODEM formar um Triângulo'
msgN = 'Os segmentos acima NÃO PODEM formar um Triângulo'

#CONDIÇÃO DE EXISTENCIA
if segA < segB + segC and segB < segA + segC and segC < segA + segB and  segA > abs(segB - segC) and segB > abs(segA - segC) and segC > abs(segA - segB):
    print(msgY)
else:
    print(msgN)

