"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com
5% de desconto.
"""
preco = float(input('Digite o preço do produto? R$ '))
desc = preco - ((5 / 100) * preco)
print('O produto que custa R${:.2f} com desconto de 5% passa a custar R${:.2f}'.format(preco, desc))
