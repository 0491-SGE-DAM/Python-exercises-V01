#!/usr/bin/python3

"""
## 006 Buscando palabras incorrectas

Entrada
-------
Una frase

Salida
------
Una lista con las palabras erróneas
"""

phrase = input()
words = phrase.split()

wrong_words = []

for word in words:
    if any(char.islower() for char in word) or any(char.isdigit() for char in word):
        wrong_words.append(word)

print(wrong_words)
