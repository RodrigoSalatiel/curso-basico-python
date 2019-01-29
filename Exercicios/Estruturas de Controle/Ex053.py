#DETECTOR DE PALÍNDROMO
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split() #splitei a frase
junto = ''.join(palavras) #juntei eliminando os espaçõs
inverso = ''


#INICIAR NA ÚLTIMA LETRA, VOLTAR ATÉ A PRIMEIRA (0 - 1) E ITERAR VOLTANDO PARA O 0
for letra in range(len(junto) - 1, -1 , -1):
    inverso += junto[letra]
print('A palavra inversa é: {}'.format(inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
