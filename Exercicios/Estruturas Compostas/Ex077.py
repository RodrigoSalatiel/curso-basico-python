palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar','trabalhar', 'mercado', 'programador', 'futuro')
for pos in palavras:
    print(f'\nNa palavra {pos} temos: ', end = '')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
