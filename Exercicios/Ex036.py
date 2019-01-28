nome = str(input("Informe o seu nome completo: ")).upper()
valorCasa = float(input('Informe o valor do imóvel: R$ '))
salario = float(input('Informe a s sua renda mensal: R$ '))
qtdParcelas = int(input('Em quantos meses deseja pagar? '))
valorPrestacao = valorCasa / qtdParcelas

print('')
print('==== CONTROLE DE EMPRÉSTIMOS ====')
print('Nome Completo: {}'.format(nome))
print('Valor do Imóvel: R$ {:.2f}'.format(valorCasa))
print('Parcelamento em {} meses'.format(qtdParcelas))
print('Valor das parcelas: R$ {:.2f}'.format(valorPrestacao))
if valorPrestacao > salario * 0.30:
    print('Situação do Pedido: NEGADO')
else:
    print('Situação do Pedido: ACEITO')