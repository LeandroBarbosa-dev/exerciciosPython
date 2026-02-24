"""
Escreva um programa que leia a velocidade
de um carro.

Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado.

A multa vai custar R$7.00 por cada
Km acima do limite.
"""

velCarro = float(input('Informe a velociade do carro Km/h: '))

if velCarro > 80:
    print('Você ultrapasso o limite de velocidade de 80Km/h')
    multa = (velCarro - 80) * 7
    print('O valor da multa é R${:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')
print('--Fim do Programa--')
