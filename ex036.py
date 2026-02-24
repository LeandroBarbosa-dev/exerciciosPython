"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ela vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
"""
print('\033[33m-=\033[m'*20)
print('{:^35}'.format('Bank LHB'))
print('\033[33m-=\033[m'*20)

valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Informe o salário do comprador: R$ '))
anos = int(input('Em quantos anos o cliente prentende pagar? '))
# Calculo da prestação:
prestacao = valor_casa / (anos * 12)

limite = salario * 0.3
if prestacao > limite:
    print('\033[33m-=\033[m' * 20)
    print('\033[31mEmpréstimo NEGADO!\033[m')
    print('A parcela é acima de 30% do salário. \nO valor da parcela seria R${:.2f}'.format(prestacao))
else:
    print('\033[33m-=\033[m' * 20)
    print('Empréstimo \033[32mAPROVADO! Parabéns\033[m')
    print('Valor da parcela ao mês R${:.2f}'.format(prestacao))
''