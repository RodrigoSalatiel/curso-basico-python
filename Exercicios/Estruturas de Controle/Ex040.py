nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
media = (nota1 + nota2) / 2

print('Média: {:.2f}'.format(media))
if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')