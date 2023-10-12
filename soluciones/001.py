#!/usr/bin/python3

"""
001 Reducción de cadenas 

Entrada
-------
Se solicita una cadena (S) y un número (N)

Salida
------
Los últimos N carácteres de la cadena S
"""

string_S = input()
string_N = input()

try:
  number_N = int(string_N)
except ValueError:
  print("##ERROR##")
  exit()

string_S = string_S.strip()

if len(string_S) < number_N:
  print("##ERROR##")
  exit()

print(string_S[-1*number_N:])