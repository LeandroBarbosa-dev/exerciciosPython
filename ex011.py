"""
Faça um programa que leia a largura e altura de uma parede em metros, calcule
a sua área e a quatidade de tinta nescessária para pintá-la, sabendo que
cada litro de tinta, pinta uma área de 2m².
"""
largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
print('=' * 45)
print('A área da sua parede é de {:.2f} m².'.format(area))
litro = area / 2
print('Você vai precisar de {:.2f} litros de tinta'.format(litro))
print('=' * 45)

