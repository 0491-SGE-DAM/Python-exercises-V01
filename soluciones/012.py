#!/usr/bin/python3

"""
# Dibujando flechas

Crea un programa que dibuje una punta de una flecha dirigida hacia la derecha.

Entrada
-------
Longitud L, dónde L > 3 y L < 10 

Salida
------
Una punta de flecha de longitud L con una línea inicial de longitud L/2
"""

width = input()
char = "X"

# chequeo de errores. height ha de ser un entero
try:
  width = int(width)
except ValueError:
  print("##ERROR##")
  exit()

# chequeo de errores. Limitación de valores
if width < 4 or width > 9:
  print("##ERROR##") 
  exit()

# Cálculo del ancho disponible
max_width = width + width // 2  

# Dibujo parte superior 
for line in range(width):
  print(" "*(width//2) + char*line)

print(char*max_width)

# Dibujo parte inferior
for line in range(width-1, 0, -1):
  print(" "*(width//2) + char*line)