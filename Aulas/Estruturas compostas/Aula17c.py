a = [2,3,4,7]
#b = a
b = a[:] #FORMA CORRETA DE COPIAR UMA LISTA, TODOS OS VALORES DE "A" SERÃO COPIADOS PARA A LISTA "B", SEM CRIAR UMA LIGAÇÃO
b[2] = 8 #A PARTIR DO MOMENTO QUE VOCÊ FAZ UMA LIGAÇÃO ENTRE AS LISTAS, AS ALTERAÇÕES SÃO FEITAS NA DUAS OU MAIS
print(f'Lista A: {a}')
print(f'Lista B: {b}')