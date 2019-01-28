somaIdade = 0
mediaIdade = 0
nomeHomemMaisVelho = ''
idadeHomemMaisVelho = 0
qtdMcomMenos20 = 0

for c in range(1,5):
    nome = str(input('Informe o nome da {}º pessoa: '.format(c))).title()
    idade = int(input('Informe a idade da {}º pessoa: '.format(c)))
    sexo = str(input('Informe o sexo da {}º pessoa[H/M]: '.format(c))).upper()

    ##MÉDIA DE IDADE
    somaIdade += idade
    mediaIdade = somaIdade / c

    #Mulheres com menos de 20
    if sexo == 'M' and idade < 20:
        qtdMcomMenos20+=1

    #NomeDoHomemMaisVelho
    if sexo == 'H' and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        nomeHomemMaisVelho = nome

print('Média de idade: {} \nHomem mais velho: {} \nQuantidade de mulheres com menos de 20 anos: {}'.format(mediaIdade, nomeHomemMaisVelho, qtdMcomMenos20))