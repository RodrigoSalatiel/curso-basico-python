from datetime import date

trabalhador = {}
idade = 0
idadeAposentadoria = 0
tempoServico = 0
trabalhador['Nome'] = str(input('Informe o nome: ')).title()
trabalhador['Idade'] = int(input('Informe o ano de nascimento[yyyy]: '))

#CALCULAR IDADE
idade = date.today().year - trabalhador['Idade']
trabalhador['Idade'] = idade
trabalhador['Nº Carteira de Trabalho'] = int(input('Nº da Carteira de Trabalho[0 - Não possui]: '))


if trabalhador['Nº Carteira de Trabalho'] == 0:
    print('-=' * 5, 'INFORMAÇÕES', '=-' * 5)
    del trabalhador['Nº Carteira de Trabalho']
    for k,v in trabalhador.items():
        print(f'{k}: {v}')
    print('Não possui Carteira de Trabalho!')
    print()
else:
    trabalhador['Ano de contratação:'] = int(input('Informe o ano de contratação[yyyy]: '))
    trabalhador['Salário'] = float(input('Informe o salário: R$'))
    # CALCULAR TEMPO DE SERVIÇO
    tempoServico = date.today().year - trabalhador['Ano de contratação:']
    idadeAposentadoria = (35 - tempoServico) + trabalhador['Idade']

    #ADICIONAR IDADE DE APOSENTADORIA AO DICIONÁRIO
    trabalhador['Idade de aposentadoria'] = idadeAposentadoria
    print('-=' * 5, 'INFORMAÇÕES', '=-' * 5)
    for k,v in trabalhador.items():
        print(f'{k}: {v}')
    print()