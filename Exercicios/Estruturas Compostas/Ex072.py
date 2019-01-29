extenso = ('zero','um','dois','três','quartro','cinco','seis','sete','oito','nove','dez','onze','doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito','dezenove','vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero >=0 and numero <= 20:
        break
    else:
        print('Tente novamente. Digite um número entre 0 e 20: ')
print(f'Você digitou o número {extenso[numero]}')
