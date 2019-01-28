import random
import playsound

numero = int(input('Digite um numero entre 1 e 5: '))
sort = random.randint(1,5)
if numero == sort:
    print('VOCÊ ACERTOU!!!')
    playsound.playsound('acertou.mp3')
else:
    print('ERROOOOOOU')
    playsound.playsound('errou.mp3')
print('Número digitado: {} \nNúmero sorteado: {}'.format(numero,sort))
