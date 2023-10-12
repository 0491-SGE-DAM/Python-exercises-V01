# Enunciados ejercicios Python. Volumen I

## 001 Reducción de cadenas 

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que solicite una cadena S y un número N t devuelva los últimos N caracteres de S. 
 * No se debe tener en cuenta los espacios que prefijen o sufijen la cadena.
 * Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

**Entrada**

Se solicita una cadena (S) y un número (N)

**Salida**

Los últimos N carácteres de la cadena S. 

### Ejemplos

<br>

> **Entrada**

```
elucubrar
5
```

> **Salida**
```
ubrar
```
<br>

> **Entrada**

```
coche
6
```

> **Salida**
```
##ERROR##
```

<hr>

## 002 Cuadrado de números 

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que solicite números enteros hasta que se introduzca _exit_ y devuelva una lista con las potencias de dos de esos números.

 * No se debe tener en cuenta los espacios que prefijen o sufijen la cadena.
 * Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

**Entrada**

Se solicita número hasta que se introduzca __exit__ (no case sensitive)

**Salida**

Una lista con los cuadrados de los número introducidos

### Ejemplo

<br>

> **Entrada**

```
4
5
2
exit
```

> **Salida**

```
[16, 25, 4]
```

<hr>

## 003 Cuadrado de números (sólo pares)

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que solicite números enteros hasta que se introduzca _exit_ y devuelva una lista con las potencias de dos de esos números sólo si esta potencia es un número par.

 * No se debe tener en cuenta los espacios que prefijen o sufijen la cadena.
 * Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

**Entrada**

Se solicita número hasta que se introduzca __exit__ (no case sensitive)

**Salida**

Una lista con los cuadrados de los número introducidos

### Ejemplo

<br>

> **Entrada**

```
4
5
2
exit
```

> **Salida**

```
[16, 4]
```

<hr>

## 004 Inviertiendo números 

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que solicite un número y lo devuelva invirtiendo el orden de los digitos.
* Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

**Entrada**

Se solicita número N

**Salida**

Un número con los dígitos de N invertidos

### Ejemplo

<br>

> **Entrada**

```
45631
```

> **Salida**

```
13654
```

<hr>

## 005 Ruleta de la fortuna

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que cambie las letras de una frase por _ en caso de la letra de la frase aparezca en la cadena de búsquedas. Indica el número de letras acertadas.

**Entrada**

Una frase y una cadena con las letras a buscar.

**Salida**

La frase con _ sustituyendo la letras acertadas y el número de letras acertadas

### Ejemplo

<br>

> **Entrada**

```
El coloso en llamas
eO
```

> **Salida**

```
_l c_l_s_ _n llamas
5
```
<hr>

## 006 Buscando palabras incorrectas

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que localice las palabras de uns frase que incluyen una o más letras en minúscula o un número.

**Entrada**

Una frase.

**Salida**

Una lista con las palabras erróneas

### Ejemplo

<br>

> **Entrada**

```
EL C0LOSO EN LlAMAS
```

> **Salida**

```
['C0LOSO', 'LlAMAS']
```
<hr>

## 007 Invirtiendo cadenas

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que invierta las letras de una cadena.

**Entrada**

Una cadena.

**Salida**

La misma cadena ordenada en orden inverso

### Ejemplo

<br>

> **Entrada**

```
Camaleón
```

> **Salida**

```
nóelamaC
```

<hr>

## 008 Serie de Fibonacci

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que muestre los N (N<=100) primeros números de la serie de Fibonacci. 
* Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

**Entrada**

Un número entre 1 y 100

**Salida**

Los N primeros dígitos de la serie de Fibonacci serparados por espacios

### Ejemplo

<br>

> **Entrada**

```
4
```

> **Salida**

```
0 1 1 2 
```

<hr>

## 009 Números pares

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que muestre los N (N<=100) primeros números pares.
* Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

**Entrada**

Un número entre 0 y 100

**Salida**

Los N primeros números pares separados por espacios

### Ejemplo

<br>

> **Entrada**

```
4
```

> **Salida**

```
0 2 4 6
```

<hr>

## 010 ¿Es primo?

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que compruebe si un número es [primo](https://es.wikipedia.org/wiki/N%C3%BAmero_primo), es decir sólo es divisible por 1 y por el mismo (el 1 no se tiene en cuenta).
* Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

### Créditos

* [aprendeaprogramar.org](https://aprendeaprogramar.org/)

### Consejo

No es neceserio comprobar todos los números, sólo hasta la raíz cuadrada del número más uno.

**Entrada**

Un número positivo

**Salida**

SI en caso de que el número sea primo, NO en caso de que no lo sea

### Ejemplo

<br>

> **Entrada**

```
11
```

> **Salida**

```
SI
```
<br>

> **Entrada**

```
9
```

> **Salida**

```
NO
```

<hr>

# 011 Dibujando árboles

## Especificaciones

Crea un programa que dibuje un árbol de una de terminada altura.
* Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

**Entrada**

Altura del árbol H, dónde H > 3 y H < 10 

**Salida**

Un árbol con la copa de altura H y el tronco de altura la parte entera de H/2

## Ejemplo

<br>

**Entrada**

5

**Salida**

\
    X\
   XXX\
  XXXXX\
 XXXXXXX\
XXXXXXXXX\
    X\
    X

<hr>

# 012 Dibujando flechas

## Especificaciones

Crea un programa que dibuje una punta de una flecha dirigida hacia la derecha.
* Realiza el control de errores y muestra como salida ##ERROR## en el caso de que un error aparezca.

**Entrada**

Longitud L, dónde L > 3 y L < 10 

**Salida**

Una punta de flecha de longitud L con una línea inicial de longitud L/2

## Ejemplo

**Entrada**

5

**Salida**

\
  X\
  XX\
  XXX\
  XXXX\
XXXXXXX\
  XXXX\
  XXX\
  XX\
  X\
