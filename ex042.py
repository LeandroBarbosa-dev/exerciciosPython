"""
Refaça o DESAFIO 035 dos triângulos, acrecentando o recurso de mostar que tipo
de triângulo será formado:

> Equilátero: todos os lados iguais
> Isósceles: dois lados iguais
> Escaleno: todos os lados diferentes
"""
print('---- Exercício Triângulo ----')

ladoA = float(input('Digite o primeiro segmento: '))
ladoB = float(input('Digite o segundo segmento: '))
ladoC = float(input('Digite o terceiro segmento: '))

if((ladoA != 0 and ladoB != 0 and ladoC != 0) and (ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB)):
    if(ladoA != ladoB and ladoB != ladoC and ladoC != ladoA):
        print('Os segmentos digitados formam um triângulo: Escaleno.')
    else:
        if(ladoA == ladoB and ladoB == ladoC and ladoC == ladoA):
            print('Os segmentos digitados formam um triângulo: Equilátero.')
        else:
            print('Os segmentos digitados forma um triângulo: Isósceles.')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')
print('Fim do programa. Encerrando...')

