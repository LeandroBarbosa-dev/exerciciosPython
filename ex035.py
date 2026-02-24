#Desenvolva um programa que leia o comprimento
#de três retas e diga ao usuário se elas podem ou não
#formar um triângulo.

print('---- Exercício Comprimento Triângulo ----')
ladoA = float(input('Digite primeiro valor: '))
ladoB = float(input('Digite o segundo valor: '))
ladoC = float(input('Digite o terceiro valor: '))

if ladoA + ladoB > ladoC:
    if ladoA + ladoC > ladoB:
        if ladoB + ladoC > ladoA:
            print('Os valores informados FORMA um triângulo!')
else:
    print('Os valores NÃO FORMA um triângulo!')
print('FIM DO PROGRAMA')
