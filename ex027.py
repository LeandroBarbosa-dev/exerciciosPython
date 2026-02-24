"""
Faça um pograma que leia o nome completo
de uma pessoa, mostrando em seguida o primeiro e o
último nome separadamente.

Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

nome = str(input('Digite seu nome completo: ')).strip()
dividir_nome = nome.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(dividir_nome[0]))
print('Seu último nome é: {}'.format(dividir_nome[-1]))
