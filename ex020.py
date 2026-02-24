"""
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
mostre a ordem sorteada.
"""
from random import shuffle

aluno1 = input('Primeiro nome: ')
aluno2 = input('Segundo nome: ')
aluno3 = input('Terceiro nome: ')
aluno4 = input('Quarto nome: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem das apresentações será')
print(lista)
