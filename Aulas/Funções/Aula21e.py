#UTILIZANDO RETURN
#DESTA FORMA O CODIGO FUNCIONA, PORÉM TERÁ ALGUMAS LIMITAÇÕES
'''def somar(a = 0, b = 0, c = 0):
    soma = a + b + c
    print(f'A soma vale {soma}')

#OS RESULTADOS SÃO EXECUTADOS SEMPRE DA MESMA FORMA
somar(3, 2, 5)
somar(2,2)
somar(4)'''

#PARA TIRAR AS LIMITAÇÕES, VAMOS UTILIZAR RETURN
def somar(a = 0, b = 0, c = 0):
    somar = a + b + c
    return somar #o valor de somar vai para dentro da variável resp

resp = somar(3, 2, 5)
print(f'A soma vale {resp}')
#o valor retornado pode tambem ser colocado diretamente dentro de um print
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
#Utilizando return, é possível colocar as informações da forma que você desejar
print(f'A 1ª soma vale {r1}, a 2ª soma vale {r2} e a 3ª soma vale {r3}')
