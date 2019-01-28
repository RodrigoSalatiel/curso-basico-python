frase = 'Curso em Vídeo Python'
print(frase)

#Funções de Transformação
print(frase.replace('Python','Android')) #Substituir os Caracteres, ou seja, a frase ficaria "Curso em Video Android
print(frase.upper())                     #Transformar todas as letras em MAIÚSCULAS
print(frase.lower())                     #Transformar todas as letras em MINÚSCULAS
print(frase.capitalize())                #Transforma somente a primeira letra da String em Maiúscula(Curso em video python)
print(frase.title())                     #Transforma todas as Iniciais em Maiúsculo de todas as palavras(Curso Em Video Python

frase2 = "   Aprenda Python  "
print(frase2.strip())  #Vai retirar os espaços inúteis(Antes e depois da Stirng, os espaçoes de separação entre palavras permanecem
print(frase2.lstrip()) #Vai retirar apenas os espaços inúteis a ESQUERDA da String
print(frase2.rstrip()) #Vai retirar apenas os espaços inúteis a DIREITA da String