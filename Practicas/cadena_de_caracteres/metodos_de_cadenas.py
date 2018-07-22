#!/usr/bin/python3    

"""
Vamos a practicar las cadenas de caracteres o metodos de cadenas ahora de nuevo ya que
este archivo.py se ha tenido que ver despues de haber dado las clases, ya que en python
se consideran una cadena de caracteres como un objeto o String.

"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"

"""
upper() pasa a mayusculas
lower() pasa a minusculas
capitalize() pone la primera letra en mayusculas
count() cuenta cuantas veces aparece una letra o cadena dentro de un texto
find() representa la posicion de un caracter o un grupo de caracteres dentro de un texto
isdigit() devuelve un boleano, y lo que nos dice es si es un valor numerico o no
isalum() comprueba si es alfanumerico
isalpha() comprueba si hay solo letras, los espacios no cuentan
split() separa por palabras utilizando espacios
strip() borrar los espacios sobrantes al principio y al final
replace() reemplaza una palabra o letra por otra dentro de un string
rfind() representa el indice de una caracter, pero este lo hace contando desde atras.

documentación de python en google
pyspanishdoc.sourceforge.net
referencia de bibliotecas en el apartado 2.1.5.1 nos aparecen todos los metodos

"""

nombreUsuario=input("Introduce el nombre: ")
print("El nombre es: ", nombreUsuario)
print("El nombre en mayusculas es: ", nombreUsuario.upper())
print("El nombre con capitalize es:" ,nombreUsuario.capitalize())

print()

edad=input("Introduce una edad ")
print("Es un numero? ", edad.isdigit())  #comprueba si es un caracter numerico

print()
while(edad.isdigit()==False):  #comprueba si es un numero y nos lo repite hast que lo introduzcamos
	print("Por favor introduce un valor numerico")
	edad=input("Introduce de nuevo tu edad: ")

if (int(edad)>18):
	print("Podemos pasar")
else:
	print("No podemos pasar")