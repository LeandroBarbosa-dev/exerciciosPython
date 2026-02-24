"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
> 1 para binário
> 2 para octal
> 3 para hexadeciaml
"""

print('\033[33m-=\033[m'*20)
print('{:^35}'.format('Conversão de base'))
print('\033[33m-=\033[m'*20)

num = int(input('Digite um valor para ver a base de conversão: '))
opcao = int(input('''
Escolha uma das opções abaixo:
[ 1 ] para Base Binária
[ 2 ] para Base Octal
[ 3 ] para Base Hexadecimal
Opção: ''' ))

if opcao == 1:
    binario = bin(num)
    print('O valor {} convertido para Binário é: {}'.format(num, binario[2:]))
elif opcao == 2:
    octal = oct(num)
    print('O valor {} convertido para Octal é: {}'.format(num, octal[2:]))
elif opcao == 3:
    hexa = hex(num)
    print('O valor {} convertido para Hexadeciaml é: {}'.format(num, hexa[2:]))
else:
    print('Opção inválida!')
print('FIM DO PROGRAMA!')