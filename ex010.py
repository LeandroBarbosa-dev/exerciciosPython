"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos Dólares ela pode comprar.

Considere:
US$1,00 = R$3,27
"""
dinheiro = float(input('Digite quanto de dinheiro você tem na carteira? R$'))
dollar = dinheiro / 3.27
print('Como essa quantia de R${:.2f} você comprar US${:.2f}'.format(dinheiro, dollar))
