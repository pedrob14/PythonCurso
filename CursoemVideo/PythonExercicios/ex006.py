# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
from math import sqrt

n = float(input('Digite um número: '))
print("Valor {}: \ndobro {} \ntriplo {} \nRaiz Quadrada {:.2f}".format(n, n * 2, n * 3, sqrt(n)))
