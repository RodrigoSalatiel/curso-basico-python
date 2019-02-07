jogador = {}
time = list()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Informe o nome do jogador: ')).title()
    totPartidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0,totPartidas):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:] #copiar conteúdo da lista partidas
    jogador['totalGols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar[S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('Opção inválida! Digite "S" ou "Npara continuar')
    if resp == 'N':
        break
print('-' * 40)
print(f'{"CÓD":^7}{"JOGADOR":<16}{"GOLS":<10}{"TOTAL GOLS":<16}')
print('-' * 40)
for k,v in enumerate(time):
    print(f'{k :^7}', end = '')
    for dado in v.values():
        print(f'{str(dado):<15}', end = '')
    print('')
print('-' * 40)

#EXIBIR DADOS INDIVIDUAIS
while True:
    op = int(input('Deseja mostrar o código de qual jogador[999 para encerrar]? '))
    print('-' * 40)
    if op == 999:
        break
    if op >= len(time):
        print('Opção inválida!')
    else:
        print(f' -- Levantamento do jogador {time[op]["nome"]}:')  # Time da opção no campo nome
        for i, gols in enumerate(time[op]['gols']):  # time da opção selecionada no campo "gols"
            print(f'    Na partida {i + 1} fez {gols} gols. ')
    print('-' * 40)

print('<< PROGRAMA ENCERRADO >>')