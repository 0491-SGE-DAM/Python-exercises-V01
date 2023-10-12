#!/usr/bin/python3

"""
## 002 Cuadrado números 

Entrada
-------
Se solicita número hasta que se introduzca exit (no case sensitive)

Salida
------
Una lista con los cuadrados de los número introducidos
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

square_list = [x * x for x in number_list]

print(square_list)