# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:25:06 2020

@author: Julio
"""

#Ambos dados muestran la misma cara
from random import randint, uniform,random

#Generación de variables aleatorias entre 1 y 6
dado1 = randint(1,6)
dado2 = randint(1,6)
#Operación
resultado = (dado1 - dado2) % 3
#Condicional
print('dado 1: ' + str(dado1))
print('dado 2: ' + str(dado2))
print('-----------------------------------------------')
if resultado == 0:
    print('La resta de ambos dados es divisible por 3')
else:
    print('La resta de ambos dados no es divisible por 3')
