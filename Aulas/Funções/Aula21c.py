#PARAMETROS OPCIONAIS
'''def soma(a,b,c): → Declarando desta forma eu obrigatoriamente precisaria digitar 3 valores, caso contr´rio, daria erro na minha aplicação
Ao utilizar parametros opcionais, eu consigo realizar as operações mesmo que falte algum parâmetro
EX:'''
def soma(a = 0, b = 0, c = 0): #declarar os parametros = 0 significa que eles serão opcionais...observe...
    soma = a + b + c
    print('-=' * 20)
    print(f'A soma é igual a {soma}')


soma(2,4,6) #3 parâmetros
soma(15, 7) #2 parâmetros
soma(10)    #1 parâmetro
soma()      #nenhum parâmetro, será utilizado o valor padrão que neste caso é ZERO
soma(c = 3, a = 2)