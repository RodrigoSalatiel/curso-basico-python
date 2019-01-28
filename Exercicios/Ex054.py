from datetime import date
maioresIdade = 0
menoresIdade = 0

for c in range(1,8):
    anoNasc = int(input('Informe o ano de nascimento da {}º pessoa: '.format(c)))
    if date.today().year - anoNasc >= 18:
        maioresIdade+=1
    else:
        menoresIdade+=1
print('Quantidade de maiores de idade: {} \nQuantidade de menores de idade: {}'.format(maioresIdade, menoresIdade))