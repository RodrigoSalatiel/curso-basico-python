'''teste = list()
teste.append('Rodrigo')
teste.append(24)
galera = list()
galera.append(teste[:]) #Copiar lista [:]
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print(galera[3][0])'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade!')'''

'''galera = list()
dado = list() #vai pegar temporariamente os dados da lista
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #Limpar a lista auxiliar
print(galera)'''

galera = list()
dado = list() #vai pegar temporariamente os dados da lista
totMaior = totMenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #Limpar a lista auxiliar

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totMaior +=1
    else:
        print(f'{p[0]} é menor de idade')
        totMenor += 1
print(f'Temos {totMaior} maiores e {totMenor} menores de idade!')