from datetime import date
anoNasc = int(input('Informe o seu ano de nascimento[yyyy]: '))
idade = date.today().year - anoNasc

if idade < 18:
    aux = 18 - idade
    print('Você terá que se alistar no Exército daqui {} ano(s)!!!'.format(aux))
elif idade == 18:
    print('Você precisa se alistas no EB NESTE ANO!')
else:
    aux = idade - 18
    print('Você deveria ter se alistado há {} ano(s)!!!'.format(aux))