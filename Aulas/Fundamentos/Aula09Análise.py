frase = 'Curso em Vídeo Python'
print(frase)

#Funções de Análise para as Strings
print(len(frase))             #Indica o Tamanho da frase(Quantidade de Caracteres(contando os espaçoes vazios)
print(frase.count('o'))       #Contar quantas vezes aparece o caracter entre parenteses(case sensitive
print(frase.count('o',0,13))  #Contagem + Fatiamento...vai buscar a letra 'o' entre os caracteres 0 e 12
print(frase.find('deo'))      #Vai localizar a sequencia e mostrar a posição que ela inicia
print(frase.find('Android'))  #Se a sequência não existir, a função vai retornar o valor -1
print('Android' in frase)     #Verificar se existe a sequencia dentro da String e vai returnar True ou False