#DECLARAR DICIONÁRIO: {} ou dict()
pessoas = {'nome': 'Rodrigo', 'sexo': 'M', 'idade': 24}
#KEYS = nome dos campos ex: nome
#VALUES = valores contidos nas keys ex:Rodrigo
#ITEMS = values + keys ex: nome: Rodrigo
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-=' * 40)
#del pessoas['sexo'] #Apagar um elemento
#pessoas['nome'] = 'Fernando' #Modificar
pessoas['peso'] = 88.9 #ADICIONAR KEY E VALUE - não é necessário utilizar append
for keys, values in pessoas.items():
    print(f'{keys} = {values}')