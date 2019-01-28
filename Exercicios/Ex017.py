import math
catetoOposto = int(input("Informe o valor do cateto oposto: "))
catetoAdjacente =  int(input('Informe o valor do caceto adjacente: '))
hipotenusa = math.sqrt(math.pow(catetoOposto,2) + math.pow(catetoAdjacente,2))
print('Cateto Oposto: {} \nCateto Adjacente: {} \nHipotenusa: {:.1f}'.format(catetoOposto,catetoAdjacente, hipotenusa))

