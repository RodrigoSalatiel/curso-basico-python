#ESCOPO DE VARIÁVEIS
'''def teste():
    x = 8
    print('Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

#PROGRAMA PRINCIPAL
n = 2
print(f'No programa principal n vale {n}')
teste()
#print(f'No programa principal x vale {x}')
# x não é uma variável de escopo global e só vai funcionar dentro da def onde foi declarada'''

'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''

#PARA ATRIBUIR UMA VARIÁVEL LOCAL A UMA VARIAVEL GLOBAL, BASTA UTILIZAR A PALAVRA GLOBAL DENTRO DA DEF
def funcao(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
funcao(a)
print(f'A fora vale {a}') #variaval "a" global deixou de valer 5 e passou a valer 8