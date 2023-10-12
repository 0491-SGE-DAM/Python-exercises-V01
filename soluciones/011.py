#!/usr/bin/python3

"""
# Dibujando árboles

Crea un programa que dibuje un árbol de una de terminada altura.

Entrada
-------
Altura del árbol H, dónde H > 3 y H < 10 

Salida
------
Un árbol con la copa de altura H y el tronco de altura la parte entera de H/2
"""

height = input()
char = "X"

# chequeo de errores. height ha de ser un entero
try:
  height = int(height)
except ValueError:
  print("##ERROR##")
  exit()

# chequeo de errores. Limitación de valores
if height < 4 or height > 9:
  print("##ERROR##") 
  exit()

# Cálculo del ancho disponible
max_width = 2 * height - 1  

# Dibujo la copa del árbol
for line in range(height):
  # centro en el ancho disponible 
  row='{:^{width}}'.format(char*(2*line+1), width=max_width)
  print(row)

# Dibujo el tronco
for line in range(height//2):
  row='{:^{width}}'.format(char, width=max_width)
  print(row)