'''valores = [] #É possivel criar uma lista vazia utilizando "[]" ou "list()"
valores.append(5)
valores.append(9)
valores.append(4)'''

'''for valor in valores: #EXIBIR OS VALORES DE OUTRA FORMA
    print(f'{valor}...', end = '')'''

'''for chave, valor in enumerate(valores):
    print(f'Na posição {chave}, encontrei o valor {valor}!')
print('Cheguei ao final da lista')'''

#LER VALORES PELO TECLADO
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for chave, valor in enumerate(valores):
    print(f'Na posição {chave}, encontrei o valor {valor}!')
print('Cheguei ao final da lista')