"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem na final de acordo com a média atingida:

> Média abaixo de 5.0: REPROVADO
> Média entre 5.0 e 6.9: RECUPERAÇÃO
> Média 7.0 ou superior: APROVADO
"""

print('\033[34m=\033[m' * 30)
print('\033[32m    Programa de Média            \033[m')
print('\033[34m=\033[m' * 30)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print('Parabéns aluno \033[32mAPROVADO\033[m. \nMédia final: {:.2f}'.format(media))
elif media < 5.0:
    print('Aluno \033[31mREPROVADO\033[m, \nMédia final: {:.2f}'.format(media))
else:
    print('Aluno de \033[33mRECUPERAÇÃO\033[m, \nMédia final: {:.2f}'.format(media))

print('\nFim do programa')

