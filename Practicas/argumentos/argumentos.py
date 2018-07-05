#!/usr/bin/python3    

"""
Vamos a probar los argumentos que se le pueden pasar al iniciar un script
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"

import sys

if __name__ == "__main__":
	print(sys.argv) 	#de esta forma imprimimos los argumentos que se le pasan por ejemplo
#ejecutamos lo siguiente
#	$ python3 argumentos.py  hola el2 el3 argumento4
# y nos da:
#	['argumentos.py', 'hola', 'el2', 'el3', 'argumento4']


if __name__=="__main__":
	if len(sys.argv) == 1: 	#vemos la longitud de los argumentos, numero de ellos
		print("Es necesario colocar por lo menos un argumento")
	else:
		print(sys.argv[1]) #esto nos da el argumento segundo que es el 1 pues empieza en 0 y el 0 es el propio nombre del archivo.py

		