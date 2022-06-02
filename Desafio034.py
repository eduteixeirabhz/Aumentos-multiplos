salario = float(input('Qual é o salário de seu funcionário? R$  '))
if salario >1250:
    salario = salario+(salario*10/100)
else:
    salario = (salario+salario*15/100)
print('Seu salário aumentará para R$ {:.2f}'.format(salario))


