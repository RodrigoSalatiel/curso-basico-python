primeiro = int(input('Informe o 1º termo da PA: '))
razaoPA = int(input('Informe a razão da PA '))
termo = primeiro
contador = 1
ultimoTermo = 0
total = 0
mais = 10 #O prgrama inicial exibe os 10 primeiros termos
while mais != 0:
    total += mais
    while contador <= total:
        print('{} → '.format(termo), end ='')
        termo += razaoPA
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados!'.format(total))

