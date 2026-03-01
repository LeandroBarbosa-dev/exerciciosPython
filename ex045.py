"""
Crie um programa que faça o computador jogar JAKENPÔ com você.
"""
from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

jogador = int(input('''Faça sua jogada:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
opção: '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

if computador == 0:
    if jogador == 0:
        print(f'EMPATE')

elif computador == 1:
    if jogador == 1:
        print(f'EMPATE')
elif computador == 2:
    if jogador == 2:
        print(f'EMPATE')
else:
    print('Opção inválida. Tente novamente!')

print(f'O joagador escolheu: {lista[jogador]}')
print(f'O computador escolheu: {lista[computador]}')

