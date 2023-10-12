#!/usr/bin/python3

"""
## 003 Cuadrado números (sólo pares)

Entrada
-------
Se solicita número hasta que se introduzca exit (no case sensitive)

Salida
------
Una lista con los cuadrados de los número introducidos siempre y cuando estos sean pares
"""

number_list = []

while True:
  number = input()

  if number.upper() == "EXIT":
    break

  try:
    number = int(number)
  except ValueError:
    print("##ERROR##")
    exit()

  # list comprehension
  number_list.append(number)

square_list = [x * x for x in number_list if x % 2 == 0]

print(square_list)