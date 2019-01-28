import random
nome1 = input('Informe o 1º nome: ')
nome2 = input('Informe o 2º nome: ')
nome3 = input('Informe o 3º nome: ')
nome4 = input('Informe o 4º nome: ')
lista = [nome1, nome2, nome3, nome4]
escolha = random.sample(lista, k = len(lista))

print('==== ORDEM DE APRESENTAÇÃO ====')
print('Ordem de apresentação: {}'.format(escolha))

