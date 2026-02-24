"""
Escreva um programa que leia um valor em metros e exiba convertido em centimetros
e milimetros.
"""
valor = float(input('Digite um valor em metros: '))
dam = valor / 10
hm = valor / 100
km = valor / 1000
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('O valor {} m é igual {} dam'.format(valor, dam))
print('O valor {} m é igual {} hm'.format(valor, hm))
print('O valor {} m é igual {} km'.format(valor, km))
print('O valor {} m é igual {} dm'.format(valor, dm))
print('O valor {} m é igual {} cm'.format(valor, cm))
print('O valor {} m é igual {} mm'.format(valor, mm))
