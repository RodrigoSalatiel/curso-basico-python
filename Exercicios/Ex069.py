qtdeMaioresIdade = qtdeHomens = qtdeMulher20 = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo[M/F]: ')).upper()
    if idade >= 18:
        qtdeMaioresIdade += 1
    if sexo == 'M':
        qtdeHomens += 1
    if sexo == 'F' and idade < 20:
        qtdeMulher20 += 1
    continuar = str(input('Você deseja continuar[S/N]? ')).upper()
    if continuar == 'N':
        break
print('-=' * 40 )
print('RESULTADO DAS PESQUISAS')
print(f'Quantidade de pessoas acima de 18 anos: {qtdeMaioresIdade} \nQuantidade de homens cadastrados: {qtdeHomens}', end = '\n')
print(f'Quantidade de mulheres com menos de 20 anos: {qtdeMulher20}')