"""
Escreva um programa que pergunte o salário de
um funcionário e calcule o valor do seu aumento.
> Para salários superiores a R$1.250,00
Calcule um aumento de 10%
> Para os inferiores ou iguais, o aumento
é de 15%.
"""
print('----- Exercício Aumento Salário ------')
sal = float(input('Qual o valor do salário do funcioário? R$'))

if sal > 1250:
    novoSal = sal + (sal * (10 / 100))
    print('Para o funcionário que recebia R${:.2f} com o aumento de 10%'.format(sal))
    print('Passa a receber R${:.2f}'.format(novoSal))
else:
    novoSal = sal + (sal * (15 / 100))
    print('Para o funcionário que recebia R${:.2f} com o aumento de 15%'.format(sal))
    print('Passa a receber R${:.2f}'.format(novoSal))
print('\nFIM DO PROGRAMA')
