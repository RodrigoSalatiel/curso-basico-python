from time import sleep

#RECEBER VARIOS VALORES E DIZER QUAL É O MAIOR
def maior(* valores):
   print('-=' * 20)
   print('Analisando os valores passados...')
   for num in valores:
       print(f'{num} ', end='', flush= True)
       sleep(0.5)
   print(f'foram informados {len(valores)} números ao todo!')
   if valores == 0:
       print('O maior valor digitado foi 0!')
   else:
       print(f'O maior valor digitado foi {max(valores)}', flush=True)
       

maior(2, 54, 324, 1209, 35, 2, 14)
maior(516, 54, 12, 3321, 18484, 1, 2, 3325, 6, 4)
maior(1541, 112, 3, 21, 231, 4)
maior(19641, 155, 151, 1, 221, 12, 34, 78)
maior(13, 2, 7, 44, 95, 659, 1, 23, 544)