cidade = input('Informe o nome da sua cidade: ')
verificar = cidade.upper().split()
if verificar[0] == 'SANTO':
    print('Sua cidade começa com a palavra SANTO')
else:
    print('Sua cidade não começa com a palavra SANTO')