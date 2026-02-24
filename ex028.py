"""
Escreva um programa que faça o computador
'pensar' em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário
venceu ou perdeu.
"""
from random import randint
from time import sleep

print('-=-' * 20)
print('Vamos Jogar!')
print('Eu pensei em um número entre 0 e 5. Tente adivinha...')
print('-=-' * 20)
opcao_pc = randint(0, 5)

escolha = int(input('Que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if escolha == opcao_pc:
    print('Parabéns! Você venceu!')
else:
    print('Ganhei! o número que pensei foi {} e não no {}!'.format(opcao_pc, escolha))
print('---Fim do Programa---')



