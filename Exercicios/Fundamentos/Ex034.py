salario = float(input('Informe o salário do funcionário: '))
novoSalario = 0
if salario > 1250.00:
    novoSalario = salario * 1.10
else:
    novoSalario = salario * 1.15
print('Salário Antigo: R$ {:.2f} \nNovo Salário com reajuste: R$ {:.2f}'.format(salario, novoSalario))