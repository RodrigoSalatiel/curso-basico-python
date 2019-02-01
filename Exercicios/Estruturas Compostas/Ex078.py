valores = list()
menorValor = maiorValor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite o {c + 1}º valor: ')))
    if c == 0:
        maiorValor = valores[c]
        menorValor = valores[c]

    else:
        if valores[c] > maiorValor:
            maiorValor = valores[c]

        if valores[c] < menorValor:
            menorValor = valores[c]

print('-' * 40)
print(f'Você digitou os seguintes valores: {valores}')
print(f'Maior valor digitado: {maiorValor} na posição ', end='')
for indice, valor in enumerate(valores):
    if valor == maiorValor:
        print(f'{indice}...')
print(f'Menor valor digitado: {menorValor} na posição ', end = '')
for indice, valor in enumerate(valores):
    if valor == menorValor:
        print(f'{indice}...')