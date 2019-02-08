def contador(i, f, p):
    #docstring é util para adicionar informações referente as funções criadas pelo próprio dev
    #deve estar logo abaixo do def e para declarar basta digitar 3 aspas duplas """
    """
    →Faz uma contagem e exibe na tela
    :param i: valor inicial da contagem
    :param f: valor final da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Rodrigo Salatiel
    """
    c = i
    while c <= f:
        print(f'{c} ', end = '')
        c += p
    print('FIM')


contador(0, 100, 10)
help(contador)