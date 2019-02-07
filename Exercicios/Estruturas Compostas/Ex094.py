listaPessoas = list()
mediaIdade = somaIdade = 0
listaMulheres = list()
listaAcimaMedia = list()
pessoa = {}
while True:
    pessoa['nome'] = str(input('Digite o seu nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Digite o sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F!')
    pessoa['idade'] = int(input('Digite a idade: '))
    somaIdade += pessoa['idade']
    listaPessoas.append(pessoa.copy())
    if pessoa['sexo'] == 'F':
            listaMulheres.append(pessoa['nome'])
    while True:
        resp = str(input('Deseja continuar[S/N]? ')).lower()
        if resp in 'sn':
            break
        print('ERRO! Digite apenas "S" ou "N')
    if resp == 'n':
        break
mediaIdade = somaIdade / (len(listaPessoas))
print(listaPessoas)
print(listaMulheres)
print(listaAcimaMedia)

#QUANTAS PESSOAS FORAM CADASTRADAS
print('-=' * 5, 'DADOS', '=-' * 5)
print(f'a) Foram cadastradas {len(listaPessoas)} pessoas!')
print(f'b) A média de idade do grupo é de {mediaIdade:.0f} anos')
print(f'c) Lista de mulheres cadastradas: ', end = '')
for nome in listaMulheres:
    print(f'{nome}, ',end='')
print('')
print(f'd) Lista de pessoas com idade acima da média: ')
for p in listaPessoas:
    if p['idade'] > mediaIdade:
        print('          ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()
print('\nENCERRADO!')