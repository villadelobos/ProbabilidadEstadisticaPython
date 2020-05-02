# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint, uniform,random

#Generación de variables aleatorias entre 1 y 6
dado1 = randint(1,6)
dado2 = randint(1,6)

resultado = (dado1 + dado2) % 2 

#Condicional que dirá si es primo o no
if resultado == 0:
    print('La suma de ambos dados es múltiplo de 2')
else:
    print('La suma de ambos dados no es múltiplo de 2')
