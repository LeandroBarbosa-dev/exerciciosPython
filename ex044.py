"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

> à vista dinheiro/cheque: 10% de desconto
> à vista no cartão: 5% de desconto
> em até 2x no cartão: preço normal
> 3x ou mais no cartão: 20% de juros
"""
from time import sleep
import os

while True:
    os.system('clear')
    print('-' * 45)
    print('       Escolha a forma de pagamento:')
    print('[1] à vista dinheiro/cheque: 10% de desconto')
    print('[2] à vista no cartão: 5% de desconto')
    print('[3] até 2x no cartão: preço normal')
    print('[4] 3x ou mais no cartão: 20% de juros')
    print('[5] Sair')
    print('-' * 45)
    opcao = int(input('Opção: '))


    if opcao == 1:
        preco = float(input('Digite o preço do produto: R$ '))
        precoFinal = preco - (preco * (10 / 100))
        print(f'Total a pagar: R${precoFinal:.2f}')

    elif opcao == 2:
        preco = float(input('Digite o preço do produto: R$ '))
        precoFinal = preco - (preco * (5 / 100))
        print(f'Total a pagar: R${precoFinal:.2f}')

    elif opcao == 3:
        preco = float(input('Digite o preço do produto: R$ '))
        print(f'Total a pagar: R${preco:.2f} \nTotal por parcela R${preco / 2:.2f}')

    elif opcao == 4:
        preco = float(input('Digite o preço do produto: R$ '))
        precoFinal = preco + (preco * (20 / 100))
        print(f'Total a pagar: R${precoFinal:.2f} \nTotal por parcela R${precoFinal / 3:.2f}')

    elif opcao == 5:
        print('Encerrando...')
        sleep(2)
        break
    else:
        print('Opção inválida. Tente novamente!')

