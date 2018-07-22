#!/usr/bin/python3    

"""
Serialización lo que hace es poder guardar colecciones y objetos en modo binario, con la ventaja
de poder distribuir mejor el codigo y a su vez cifrado.
Esto lo realizamos con la libreira pickle
La orden pickle.dump(lo_que_se_vuelca, nombre_fichero_memoria) lo que hace es volcar en el fichero de 
memoria lo que se le pasa en el primer argumento, porque ne el segundo se le pasa el nombre
del fichero de memoria donde volcar.

Con la orden coleccion=pickle.load(Nombre_fichero_en_memoria) lo volcamos en coleccion
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


import pickle

lista_nombres=["Pedro", "Maria", "Pepe", "Isabel"]

fichero_binario=open("lista_nombres", "wb") #fichero_binario es el fichero en memoria
											#lista_nombres es el nombre del fichero o 
											#archivo que nos queda guardado en memoria
											#la wb es write binary

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()
# incluso lo podemos borrar ya pues no nos hace falta de la memoria
del(fichero_binario) #borra de la memoria

#Hasta aquí parece que nos nos ha hecho nada, pero lo que nos hizo es crear el fichero
#binario, lo unico que nos hace falta es mostrarlo, y para no hacerlo desde un nuevo
#programa lo hago desde este mismo la lectura.

fichero=open("lista_nombres", "rb") #esta vez le hemos cambiado el nobmre del fichero en memoria
									# y la rb es de read binary

lista=pickle.load(fichero) 	# con esta orden recuperamos de un archivo binario "fichero" 
							#y lo pasamos a lista

print(lista)