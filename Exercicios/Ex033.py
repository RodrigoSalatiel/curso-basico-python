n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
n3 = int(input('Informe o 3º número: '))
maior = 0
menor = 0
if n1 <= n2 and n1 <=n3 and n2 <= n3:
    menor = n1
    maior = n3
elif n1 <= n2 and n1 <= n3 and n3 <= n2:
    menor = n1
    maior = n2
elif n2 <= n1 and n2 <= n3 and n1 <= n3:
    menor = n2
    maior = n3
elif n2 <= n1 and n2 <= n3 and n3 <= n1:
    menor = n2
    maior = n1
elif n3 <= n1 and n3 <= n2 and n1 <= n2:
    menor = n3
    maior = n2
else:
    menor = n3
    maior = n1

print('Menor valor digitado: {} \nMaior valor digitado: {}'.format(menor, maior))
