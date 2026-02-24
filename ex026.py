"""
Faça um progama que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra 'A'.
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""
frase = str(input('Digite um frase: ')).upper().strip()
print('A letra "A" aparece: {} vezes.'.format(frase.count('A')))
print('A letras "A" aparece pela primeira vez na posição: {}'.format(frase.find('A') + 1))
print('A última posição que a letra "A" aparece é: {}'.format(frase.rfind('A') + 1))
