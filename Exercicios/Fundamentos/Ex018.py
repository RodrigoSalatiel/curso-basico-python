import math
angulo = int(input('Informe o valor do Ângulo[0°-360°] : '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('Ângulo: {}° \nSeno: {:.2f} \nCosseno: {:.2f} \nTangete: {:.2f}'.format(angulo,seno,cosseno,tangente))