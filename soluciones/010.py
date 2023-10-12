#!/usr/bin/python3

"""
## 010 ¿Es primo?

Entrada
-------
Un número positivo

Salida
------
SI en caso de que el número sea primo, NO en caso de que no lo sea
"""

# importamos sqrt para realizar raiz cuadrada
from math import sqrt

number = input()

try:
  number = int(number)
except ValueError:
  print("##ERROR##")
  exit()

if number < 0:
  print("##ERROR##")
  exit()

is_prime = True

# si es par no es primo
if number % 2 == 0 and number != 2:
	is_prime = False

# parto de 3 y cada 2 para quitar los pares
# no hace falta comprobar todos los números hasta el número, 
# solo hasta la raíz cuadrada del número + 1
for i in range(3, int(sqrt(number)) + 1, 2):
	if number % i == 0:
		is_prime = False

if is_prime == True and number != 1:
	print("SI")
else:
	print("NO")
