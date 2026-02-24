"""
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria de acordo com a idade.

> Até 9 anos: MIRIM
> Até 14 anos: INFANTIL
> Até 19 anos: JUNIOR
> Até 25 anos: Sênior
> Acima: MASTER
"""
from datetime import date

print('\033[34m=\033[m' * 50)
print('\033[32m    Programa Confederação Nacional de Natação            \033[m')
print('\033[34m=\033[m' * 50)

anoNascimento = int(input('Digite o ano de nascimento do atleta: '))

# Calculo para saber a idade do atleta
idade = date.today().year - anoNascimento

# Estrututa Condicional para categoria da idade
if idade <= 9:
    print('O atleta tem {} anos, a categoria: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, a categoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos, a categoria: JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos, a categoria: SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos, a categoria: MASTER'.format(idade))
print('Fim do programa')
