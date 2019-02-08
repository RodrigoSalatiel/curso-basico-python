def notas(nota , bolSit = False):
    """
    ->Calcular quantidade de notas digitadas, maior nota, menor nota e a média do aluno
    :param nota: Recebe as notas informadas no sistema
    :param bolSit: Verificar se o usuário deseja receber informações sobre a Situação do aluno ou não
    :return: Lista com a quantiddade de notas digitadas, maior nota, menor nota e a média do aluno
    """
    total = 0
    soma = 0
    media = 0
    sit = ''
    for num in nota:
        total += 1
        soma += num
    media = soma / total
    if media >= 6:
        sit = 'APROVADO'
    else:
        sit = 'REPROVADO'
    aluno = {'Total': total, 'Maior': max(nota), 'Menor': min(nota), 'Média': f'{media:.1f}'}
    if bolSit:
        aluno['Situação'] = sit
    return aluno

#PROGRAMA PRINCIPAL
listaNotas = list()
bolSit = False
while True:
    listaNotas.append(float(input('Digite uma nota: ')))
    while True:
        resp = str(input('Deseja digitar outra nota[S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('Opção inválida! Digite apenas "S" ou "N"')
    if resp == 'N':
        while True:
            show = str(input('Deseja exibir a situação do aluno[S/N]? ')).upper()[0]
            if show in 'SN':
                break
            print('Opção inválida! Digite apenas "S" ou "N"')
        if show == 'S':
            bolSit = True
        break
aluno = notas(listaNotas, bolSit)
print(aluno)