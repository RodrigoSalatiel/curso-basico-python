sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo[M/F]: ')).upper()
    print('Sexo inválido! Informe um sexo válido[M/F]: ')
print('PROGRAMA ENCERRADO! \nSexo informado: {}'.format(sexo))