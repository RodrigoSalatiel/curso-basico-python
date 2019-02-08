def ficha(jogador = '', gols = 0):
    if jogador == '':
        jogador = '<desconhecido>'
    return f'O jogador {jogador} fez {gols} gol(s) no Campeonato Brasileiro'



#PROGRAMA PRINCIPAL
jogador = str(input('Digite o nome do Jogador: ')).title().strip()
gols = str(input('Informe a quantidade de gols marcados: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(ficha(jogador, gols))