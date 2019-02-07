aluno = {}
aluno['Nome'] = str(input('Informe o nome do aluno: ')).title()
aluno['Media'] = float(input('Informe a média do aluno: '))
situacao = ''
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'APROVADO'
else:
    aluno['Situacao'] = 'REPROVADO'

for k,v in aluno.items():
    print(f'{k}: {v}')
