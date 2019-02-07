jogador = {}
listaGols = list()
jogador['Nome'] = str(input('Nome do jogador: ')).title()
qtdePartidas = int(input('Quantidade de partidas disputadas: '))
c = 1
totalGols = 0
while c <= qtdePartidas:
    num = int(input(f'Quantos gols na {c}º partida? '))
    totalGols += num
    listaGols.append(num)
    c += 1
jogador['Gols'] = listaGols.copy()
jogador['Total gols'] = totalGols
print('-=' * 40)
print(jogador)
print('-=' * 40)
print(f"O Jogador {jogador['Nome']} jogou {qtdePartidas} partidas")
for i, v in enumerate(listaGols):
    print(f'→ Na partida {i + 1}, fez {v} gols')
print(f'Total de gols: {totalGols}')
