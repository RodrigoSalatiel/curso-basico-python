nomeCompleto = input('Informe o nome completo: ')

print(nomeCompleto.upper().strip())
print(nomeCompleto.lower().strip())
lista = nomeCompleto.split()
print('Seu nome ao todo possui {} letras'.format(len(nomeCompleto) - nomeCompleto.count(' ')))
print('Seu primeiro nome possui {} letras'.format(len(lista[0])))
