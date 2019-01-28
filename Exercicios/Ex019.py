import random
nome1 = input('Informe o nome do 1º aluno: ')
nome2 = input('Informe o nome do 2º alunos: ')
nome3 = input('Informe o nome do 3º aluno: ')
nome4 = input('Informe o nome do 4º aluno: ')

escolha = random.choice([nome1, nome2, nome3, nome4])

print('{}, você foi o escolhido para a missão!!'.format(escolha))


