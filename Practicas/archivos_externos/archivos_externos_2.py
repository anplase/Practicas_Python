#!/usr/bin/python3    

"""
En este archivo vamos a probar los punteros de los archivos externos
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
 
archivo_texto=open("archivo.txt", "r") 	#Ponemos el nombre del archivo a crear y abrir, lo hace
										# a la vez las dos cosas y la w es para escribir
										# este es el modo escritura

#frase=("Hace un día estupendo para estudiar python \nhoy sabado") #variable a guardar

#archivo_texto.write(frase) # lo que hace es escribir en el archivo_texto la variable frase,
							# de donde el archivo_texto no es el nombre, el nombre es archivo.txt que
							# esta en la primera linea donde se invocaba a open.
print(archivo_texto.read())

print("Si no se dice nada nos imprime el archivo entero, por ello vamos a ver los punteros")
print("que no es mas que decir donde empieza a leer dicho archivo")
print("Por defecto el comienzo es la primera y termina en la ultima.")

print()

print("Volvemos a escribir print(archivo_texto.read()) y no lo vuelve a ejecutar pues")
print("el puntero ha empezado y terminado ya")

print(archivo_texto.read())#este no l imprime ya que el puntero ha recorrido desde el 
							# inicio hasta el final en la lectura anterior y ahora se
							#encuentra al final con lo que por muhcas veces que lo
							#llamamemos no nos mostrará nada. Primero deberiamos llebar el
							#puntero al inicio o otra posición para que empiece de nuevo

print()
print("Vamos a leer desde la posición 10")
print()
archivo_texto.seek(11) #la orden seek es llevar el puntero a la posición que se le dice

print(archivo_texto.read()) #Volvemos a hacer la lectura pero desde la posición 

#seek lo unico que hace es posicionar el puntero
# y read si se le escribe algo dentro escribe hasta esa posición por ejemplo
print()
print("ahora imprimimos un trozo, con seek le decimos donde empieza y con read donde termina")
print()
archivo_texto.seek(8)
print(archivo_texto.read(36)) # En este caso por ejemplpo se ha quedado el puntero en la
								# posición 36, si volvemos a llamar se imprimiria desde
								#la 36 hasta el final si no se le dice nada de nuevo

print()
print("Ahora vamos a decir que nos lea la mitad justo de un archivo de texto")
print()
archivo_texto.seek(len(archivo_texto.read())/2) #tomamos la longitud del fichero de texto y
												# lo dividimos por dos
print(archivo_texto.read())

print()
print("podemos colocar el cursor al final de la primera linea por ejemplo")
print()
archivo_texto.seek(len(archivo_texto.readlines()))
print(archivo_texto.read())

archivo_texto.close() #cerramos el archivo.	


#si queremos no solo abrir el fichero en modo lectura sino tambien en modo escritura
archivo_texto=open("archivo.txt", "r+") #la r+ significa que es lctura y escritura
# con lo que a partir de aqui si escribimos y no modificamos el seek escribimos en el inicio

lista_texto=archivo_texto.readlines();

lista_texto[1]="Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

a=archivo_texto.writelines(lista_texto)

archivo_texto.close()						

print(a)