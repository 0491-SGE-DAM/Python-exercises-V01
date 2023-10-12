#!/usr/bin/python3

"""
## 009 Números pares

Entrada
_______
Un número entre 0 y 100

Salida
______
Los N primeros pares separados por espacios
"""

number_digits = input()

try:
  number_digits = int(number_digits)
except ValueError:
  print("##ERROR##")
  exit()

if number_digits < 0 or number_digits > 100:
  print("##ERROR##")
  exit()

for digit in range(0, 2*number_digits, 2):
  print(digit, end=" ")

print()