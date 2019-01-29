#VARIÁVEIS COMPOSTAS
#Tupla fica entre parenteses - NO PYTHON NOVO FUNCIONA SEM ()
#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#bebida = 'Refrigerante', 'Cerveja', 'Agua'
#print(lanche)
#print(lanche[1])
#print(lanche[-2])
#print(lanche[1:3])
#print(bebida)

#TUPLAS SÃO IMUTÁVEIS
#lanche[1] = 'Refrigerante'
#print(lanche[1]) #Gerar um erro

#Exibir dados utilizando for - 2 formas
#for comida in lanche:
#    print(f'Eu vou comer {comida}')

#for pos, comida in enumerate(lanche): #Pode ser utilizado dessa forma para mostrar a posição
#    print(f'Eu vou comer {comida} na posição {pos}')

#for contador in range(0,len(lanche)): #Muito utilizado quando tem necessidade de mostrar a posição
#    print(f'Eu vou comer {lanche[contador]}')

#Exibir a tupla em ordem
#print(sorted(lanche))

#print('Comi pra caramba!')

'''a = (2,5,4)
b = (5,8,1,2)
c = a + b #Vai juntar uma tupla na outra - a ordem tem total influência
print(c.count(2)) #Conta quantas vezes o numero aparece
print(c.index(8)) #Em que posição está o 8?
print(c.index(5, 1)) #1 correponde que a contagem vai iniciar no index 1, pulando o primeiro 5 e exibindo a posição do 2º nr 5'''

pessoa = ('Gustavo', 39, 'M', 99.88) #É possível ter dados de tipos diferentes na mesma tupla
#del(pessoa) #Não é possível alterar os elementos da tupla, mas é possível excluír a tupla inteira utilizando o comando "del"
print(pessoa)

