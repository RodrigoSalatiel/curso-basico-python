expressao = str(input('Digite uma expressão: '))
listaParenteses = list()
for simbolo in expressao:
    if simbolo == '(':
        listaParenteses.append('(')
    elif simbolo == ')':
        if len(listaParenteses) > 0:
            listaParenteses.pop()
        else:
            listaParenteses.append(')')
            break

if len(listaParenteses) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')