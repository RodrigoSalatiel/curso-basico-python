import playsound
nome = input('Digite seu nome: ')
if nome == 'Rodrigo':
    print('Você é o bichao mesmo doido')
    playsound.playsound('acertou.mp3')
else:
    print('Você é vacilãão, sai fora!')
    playsound.playsound('errou.mp3')

