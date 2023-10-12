#!/usr/bin/python3

"""
## 004 Inviertiendo números 

Entrada
-------
Se solicita número N

Salida
------
Un número con los dígitos de N invertidos
"""

number = input()

try:
  number = int(number)
except ValueError:
  print("##ERROR##")
  exit()

while number > 0:
    digit = number % 10
    # eliminar el último dígito
    number = number // 10
    print(digit, end="")

print("")