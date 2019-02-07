#CRIAR DICIONARIO DENTRO DE UMA LISTA
'''estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado3 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado4 = {'uf': 'Paraná', 'sigla': 'PR'}
brasil = list()

#Criar lista contendo os dicionarios
brasil.append(estado1)  #indice 0 da lista
brasil.append(estado2)  #indice 0 da lista
brasil.append(estado3)  #indice 0 da lista
brasil.append(estado4)  #indice 0 da lista

print(estado1)
print(brasil)
print(brasil[1])
print(brasil[1]['uf']) #no indice 1 da lista Brasil, exibir o conteudo da Key especificada'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper()
    brasil.append(estado.copy()) #Semelhante ao  [:] da lista...é necessário fazer para registrar corretamente
print(brasil)

for estado in brasil:   #for para a lista
    for key, value in estado.items():    #for para o dicionário
        print(f'O campo {key} tem valor {value}', end = ' ')
    print()
