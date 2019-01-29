equipes = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo','Atlético MG', 'Atlético PR', 'Cruzeiro','Botafogo','Santos','Bahia','Fluminense',
           'Corinthians','Chapecoense','Ceará SC','Vasco da Gama','Sport Recife','América MG', 'EC Vitória', 'Paraná')
#EXIBIR
#A) Apenas os 5 primeiros colocados
print(f'5 Primeiros colocados: {equipes[:5]}')

#B) Os últimos quatro colocados da tabela
print(f'Os últimos 4 colocados da tabela: {equipes[-4:]}')

#C) Lista com as equipes em ordem alfabética
print(f'Lista em Ordem Alfabética: {sorted(equipes)}')

#D) Em qual posião da tabela está a equipe da Chapecoense
print(equipes.index('Chapecoense'))