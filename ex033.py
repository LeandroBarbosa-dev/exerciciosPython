"""
Faça um programa que leia três números e mostre qual é o MAIOR
e qual é o MENOR.
"""
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digie o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('O MAIOR número é o {}'.format(num1))
if num2 > num1 and num2 > num3:
    print('O MAIOR número é o {}'.format(num2))
if num3 > num1 and num3 > num2:
    print('O MAIOR número é o {}'.format(num3))

if num1 < num2 and num1 < num3:
    print('O MENOR número é o {}'.format(num1))
if num2 < num1 and num2 < num3:
    print('O MENOR número é o {}'.format(num2))
if num3 < num1 and num3 < num2:
    print('O MENOR número é o {}'.format(num3))