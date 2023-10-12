#!/usr/bin/python3

"""
## 005 Ruleta de la fortuna

Entrada
-------
Una frase y una cadena con las letras a buscar.

Salida
------
La frase con _ sustituyendo la letras acertadas y el número de letras acertadas
"""

phrase = input()
letters_test = input()

letters_test_upper = letters_test.upper()
letters_test_lower = letters_test.lower()

phrase_res = [ "_" if letter in letters_test_upper or letter in letters_test_lower else letter for letter in phrase]

print(''.join(phrase_res))
print(phrase_res.count("_"))