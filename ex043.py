"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status, de acordo com a tabela abaixo:

> Abaixo de 18.5: Abaixo do peso
> Entre 18.5 e 25: Peso ideal
> 25 até 30: Sobrepeso
> 30 até 40: Obesidade
> Acima de 40: Obesidade mórbida
"""
print('=-=' * 10)
print('       Calculo de IMC')
print('=-=' * 10)

peso = float(input('Digite seu peso [ex.: 69.2]: '))
altura = float(input('Digite sua altura [ex.: 1.70]: '))

#Calculo de IMC:
imc = peso / (altura * altura)
print(f'Seu IMC é de {imc:.1f}.')
if(imc < 18.5):
    print('Você está ABAIXO DO PESO.')
elif(imc < 25):
    print('Parabéns, você está com o PESO IDEAL.')
elif(imc < 30):
    print('Você está com SOBREPESO.')
elif(imc < 40):
    print('Você está com OBESIDDE.')
else:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')
