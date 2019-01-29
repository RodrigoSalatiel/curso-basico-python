from math import pow
#CÁLCULO DE IMC
peso = float(input('Informe o seu peso(kg): '))
altura = float(input('Informe sua altura(m): '))
imc = peso / (pow(altura,2))
print('IMC: {:.1f}'.format(imc))
if imc < 18.5:
    aux = 'ABAIXO DO PESO'
elif imc >= 18.5 and imc < 25:
    aux = 'PESO IDEAL'
elif imc >= 25 and imc <30:
    aux = 'SOBREPESO'
elif imc >= 30 and imc <40:
    aux = 'OBESIDADE'
else:
    aux = 'OBESIDADE MÓRBIDA'

print('STATUS: {}'.format(aux))