"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus
Fahrenheit.
"""
c = float(input('Informe a temperatura em °C: '))
f = (c * (9 / 5)) + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(c, f))
