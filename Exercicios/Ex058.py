from random import randint
import playsound

computador = randint(0,10)
acertou = False
totTentativas = 0
while not acertou:
    jogador = int(input('Qual o seu palpite para um valor entre 0 e 10? '))
    totTentativas += 1
    if jogador == computador:
        acertou = True
    else:
        print('Errou, tente novamente!')
        playsound.playsound('errou.mp3')
print('VOCÊ ACERTOU! \nUtilizou {} tentativas para acertar!'.format(totTentativas))
playsound.playsound('acertou.mp3')