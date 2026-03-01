"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

> à vista dinheiro/cheque: 10% de desconto
> à vista no cartão: 5% de desconto
> em até 2x no cartão: preço normal
> 3x ou mais no cartão: 20% de juros
"""
print('{:=^40}'.format(' LOJAS BARBOSA '))

preco = float(input('Digite o preço do produto: R$ '))

print('Escolha a forma de pagamento:')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
print('-' * 45)
opcao = int(input('Opção: '))

if opcao == 1:
    precoFinal = preco - (preco * (10 / 100))
    print(f'Total a pagar: R${precoFinal:.2f}\n')

elif opcao == 2:
    precoFinal = preco - (preco * (5 / 100))
    print(f'Total a pagar: R${precoFinal:.2f}\n')

elif opcao == 3:
    parcela = int(input('Quantas parcelas: '))
    preco_parcela = preco / parcela
    print(f'Total a pagar: R${preco:.2f}')
    print(f'Sua comprada parcelada em {parcela}x de R${preco_parcela:.2f}.\n')

elif opcao == 4:
    parcela = int(input('Quantas parcelas: '))
    precoFinal = preco + (preco * (20 / 100))
    preco_parcela = precoFinal / parcela
    print(f'Sua compra parcelada em {parcela}x de R${preco_parcela:.2f}')
    print(f'Sua compra de R${preco:.2f} vai custar R${precoFinal:.2f} no final. COM JUROS\n')

else:
    print('Opção inválida. Tente novamente!')

