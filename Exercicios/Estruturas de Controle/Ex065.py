
menorValor = 0
maiorValor = 0
contador = 0
media = 0.0
soma = 0
n = 0
resp = ''
while resp != 'n':
    n = int(input('Digite um número: '))
    soma += n
    contador += 1
    media = soma / contador
    #maior e menor valor
    if contador == 1:
        maiorValor = n
        menorValor = n
    else:
        if n > maiorValor:
            maiorValor = n
        if n < menorValor:
            menorValor = n
    resp = str(input('Quer continuar?[S/N]: ')).lower()
print('Você digitou {} número(s) e a média entre eles foi igual a {:.2f}'. format(contador, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maiorValor, menorValor))