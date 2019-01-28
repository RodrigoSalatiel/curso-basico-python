nome = input('Digite o seu nome completo: ').strip()
listaNome = nome.split()
print('Nome completo: {} \nPrimeiro nome: {} \nÚltimo nome: {}'.format(nome, listaNome[0], listaNome[-1]))