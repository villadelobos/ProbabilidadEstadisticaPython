# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint, uniform,random

#Generación de variables aleatorias entre 1 y 6
dado1 = randint(1,6)
dado2 = randint(1,6)
#Función que hace el proceso para ver si es un número es primo
def numero_primo(dado):
    resultado2 = dado % 2 
    resultado3 = dado % 3
    resultado5 = dado % 5
    resultado7 = dado % 7
    resultado11 = dado % 11
    
    if resultado2 == 0:
        return True
    elif resultado3 == 0:
        return True
    elif resultado5 == 0:
        return True
    elif resultado7 == 0:
        return True
    elif resultado11 == 0:
        return True
    else:
        return False

cara1 = numero_primo(dado1)
cara2 = numero_primo(dado2)
#Condicional que dirá si es primo o no
if cara1 and cara2:
    print('Ambas caras del dado son números primos')
else:
    print('Ambas caras del dado no son números primos')

