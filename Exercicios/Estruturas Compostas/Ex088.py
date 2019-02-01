from random import randint

print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
temp = list()
jogos = list()
qtdeJogos = int(input('Quantos jogos você quer sortear? '))
total = 1
while total <= qtdeJogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    total += 1
print('-=' * 3,f'SORTEANDO {qtdeJogos} JOGOS', '-=' * 3)

for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')