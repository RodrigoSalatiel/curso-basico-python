def soma(* valores): #* vai indicar que o usuário pode digitar quantos números ele quiser
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(2, 4, 6, 7, 10)
soma(2, 5)
soma(3, 7, 12, 15)