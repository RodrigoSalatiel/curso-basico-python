ficha = list()

while True:
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 2: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [ nota1, nota2], media])
    resp = str(input('Quer continuar[S/N?] ')).lower()
    if resp == 'n':
        break
print('-=' * 40)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 40)
#EXIBIR ALUNO E AS MEDIAS
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 40)
    opcao = int(input('Deseja mostar as notas de qual aluno[999 interrompe]? '))
    if opcao == 999:
        break
    if opcao < len(ficha):
        print(f'Nome: {ficha[opcao][0]} \nNotas: {ficha[opcao][1]}')
    else:
        print('Valor inválido. Digite o valor corresponde aos alunos na lista: ')
print('Volte sempre!')

