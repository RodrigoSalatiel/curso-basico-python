##LISTA É MUTÁVEL!!!
num = [2,5,9,1]
num[2] = 3
#num[4] = 7 #NÃO É POSSIVEL ADICIONAR  VALORES DESSA FORMA..DEVE-SE USAR APPEND OU INSERT
num.append(7)
num.insert(2, 2) #ADICIONAR O NUMERO 8 NA POSIÇÃO 2
#num.sort() #COLOCAR OS VALORES EM ORDEM
#num.sort(reverse=True) #COLOCAR OS VALORES NA ORDEM INVERSA(MAIOR PARA O MENOR)
#num.pop(2) #SE NÃO UTILIZAR PARAMETROS, ELE VAI ELIMINAR O ULTIMO VALOR DA LISTA
#num.remove(2) #ELIMINA O PRIMEIRO NÚMERO 2 DA LISTA
if 4 in num: #CONDIÇÃO QUE APAGA O VALOR APENAS SE ELE ESTIVER NA LISTA(CASO CONTRÁRIO VAI ACUSAR ERRO)
    num.remove(4)
else:
    print('O número 4 não está na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos!')