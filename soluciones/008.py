#!/usr/bin/python3

"""
## 008 Serie de Fibonacci

Entrada
_______
Un número entre 1 y 100

Salida
______
Los N primeros dígitos de la serie de Fibonacci serparados por espacios
"""

number_digits = input()
digit_1 = 0
digit_2 = 1

try:
  number_digits = int(number_digits)
except ValueError:
  print("##ERROR##")
  exit()

if number_digits < 1 or number_digits > 100:
  print("##ERROR##")
  exit()

for digit in range(number_digits):
  print(digit_1, end=" ")
  new_digit = digit_1 + digit_2

  digit_1 = digit_2
  digit_2 = new_digit

print()