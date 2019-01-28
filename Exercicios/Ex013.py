sal = float(input('Informe o Salário do funcionário: '))
aum = float(input("Informe a % de aumento: "))
print('Salário Antigo: R${:.2f} \n% de aumento: {}% \nSalário com reajuste: R${:.2f}'.format(sal, aum , ((aum/100)+1) * sal))