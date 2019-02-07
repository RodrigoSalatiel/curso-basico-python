from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3':randint(1,6),
        'Jogador4':randint(1,6)}
ranking = list() #Será utilizada para colocar os valores em ordem
print('-=' * 4, 'VALORES SORTEADOS' , '-=' * 4)
for key,value in jogo.items():
    print(f'{key} tirou {value} no dado!')
    sleep(1)
print('-=' * 30)
print('RANKING DOS JOGADORES')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse= True ) #itemgetter(1) vai ordenar através dos valores, (0) iria rankear através das keys
for indice, valor in enumerate(ranking):  #Deve ser tratado como uma lista
    print(f'{indice + 1}º Lugar: {valor[0]} com {valor[1]} no dado!')
print()