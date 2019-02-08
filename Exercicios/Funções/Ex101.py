
def voto(anoNasc):
    from datetime import date
    idade = date.today().year - anoNasc
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos: NÃO PODE VOTAR'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO'
    return msg

#PROGRAMA PRINCIPAL
anoNasc = int(input('Digite o ano de nascimento: '))
print(f'{voto(anoNasc)}')