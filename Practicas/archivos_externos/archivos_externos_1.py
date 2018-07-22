#!/usr/bin/python3    

"""
Vamos a empezar a practicar con los archivos externos, en este caso
siempre se realizan cuatros passos.
Creamos, Abrimos, tratamos o manipulamos, y cerramos el archivo
por otro lado se recomienda utilizar la documentación de la pagina siguiente

Fijaros que en archivo_texto no es la variable a imprimir, esto solo hace la llamada
al tipo de archivo y realiza la apertura primero, luego la lectura, el cierre, 
de donde la apertura es con un igual y la lectura, cierre es con un . 
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


from io import open #Se importa la libreria io que es con la que se puede tratar los archivos
 
archivo_texto=open("archivo.txt", "w") 	#Ponemos el nombre del archivo a crear y abrir, lo hace
										# a la vez las dos cosas y la w es para escribir
										# este es el modo escritura

frase=("Hace un día estupendo para estudiar python \nhoy sabado") #variable a guardar

archivo_texto.write(frase) # lo que hace es escribir en el archivo_texto la variable frase,
							# de donde el archivo_texto no es el nombre, el nombre es archivo.txt que
							# esta en la primera linea donde se invocaba a open.

archivo_texto.close() #cerramos el archivo.							

print("Hasta aquí se ha creado, abierto, manipulado y cerrado del archivo")
print("Ahora vamos a abrir lo y leer su contenido y lo mostramos en pantalla")
print()

archivo_texto=open("archivo.txt", "r") # ahora ponemos una r de read, para leerlo

texto=archivo_texto.read() #lee lo que hay dentro del archivo de texto y lo almacena en 
							# texto
archivo_texto.close() # cerramos el archivo

print(texto)

print("ya hemos leido y cerrado el archivo de texto, ahora vamos a probar el readlines()")
print("que es leer linea a linea para ver que hace")

archivo_texto=open("archivo.txt", "r")
texto_nuevo=archivo_texto.readlines()
archivo_texto.close()

print(type(texto_nuevo))
print("Como lo convierte en lista, nos separa por el separador barra invertida y n")

print("Primer elemento de la lista",texto_nuevo[0])
print("Segundo elemento de la linea",texto_nuevo[1])

print()
print("Ahora vamos a abrir un archivo para agregar información")
print()

archivo_texto=open("archivo.txt", "a") # la a ahora es de append que es añadir

archivo_texto.write("\n siempre es un buen día para estudiar python")

archivo_texto.close()

print("Le hemos añadido una línea más")

archivo_texto=open("archivo.txt","r")
nueva_linea=archivo_texto.read()

print(nueva_linea) #abrimos para leer y mostrarlo
archivo_texto.close() # cerramos de nuevo








