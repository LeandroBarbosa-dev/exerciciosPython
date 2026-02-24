"""
Faça um programa que leia o ano de nascimento de um jovem e informa de acordo com sua idade:

> Se ele AINDA VAI SE ALISTAR ao serviço militar.
> Se é a HORA DE SE ALISTAR.
> Se já PASSOU DO TEMPO do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
from traceback import print_tb

print('\033[34m=\033[m' * 30)
print('\033[32m    Programa de Alistamento            \033[m')
print('\033[34m=\033[m' * 30)

atual = date.today().year
ano_nascimento = int(input('Informe o ano de nascimento do jovem: '))
idade = 2017 - ano_nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, idade, atual))

if idade == 18:
    print('\033[32mEstá na hora de você se alistar ao serviço militar.\033[m')
elif idade < 18:
    tempo_utrapassado = 18 - idade
    print('Ainda faltam \033[34m{} anos\033[m para você se alistar ao serviço militar.'.format(tempo_utrapassado))
    ano = atual + tempo_utrapassado
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    tempo_utrapassado = idade - 18
    print('Já passou o tempo de \033[31m{} anos\033[m de você se alistar ao serviço militar.'.format(tempo_utrapassado))
    ano = atual - tempo_utrapassado
    print('Seu alistamento foi em {}'.format(ano))
