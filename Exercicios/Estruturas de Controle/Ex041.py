from datetime import date

anoNasc = int(input('Informe o ano de nascimento do atleta[yyyy]: '))
idade = date.today().year - anoNasc
print('Idade: {}'.format(idade))
if idade < 9:
    cat = 'MIRIM'
elif idade >=9 and idade <14:
    cat = 'INFANTIL'
elif idade >=14 and idade <19:
    cat = 'JÚNIOR'
elif idade >=19 and idade <= 20:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print('Categoria: {}'.format(cat))
