"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
num = int(input('Digite um valor: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1 / 2)
print('O dobro de {} vale {}.'.format(num, dobro))
print('O triplo de {} vale {}.'.format(num, triplo))
print('A raiz quardada de {} é igual {:.2f}.'.format(num, raiz))
