pessoas = list()
dado = list() #Lista auxiliar
maiorPeso = menorPeso = 0
maisLeves = list()
maisPesados = list()

while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Informe o peso[kg]: ')))
    if len(pessoas) == 0:
        maiorPeso = dado[1]
        menorPeso = dado[1]
    else:
        if dado[1] > maiorPeso:
            maiorPeso = dado[1]
        if dado[1] < menorPeso:
            menorPeso = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar? [S/N]')).lower()
    if resp == 'n':
        break

for p in pessoas:
    if p[1] == maiorPeso:
        maisPesados.append(p[0])
    if p[1] == menorPeso:
        maisLeves.append(p[0])


print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'{maisPesados} são os mais pesados, pesando {maiorPeso} kg')
print(f'{maisLeves} são os mais leves, pesando {menorPeso} kg')

