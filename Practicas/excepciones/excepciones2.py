#!/usr/bin/python3    

"""
Vamos a practicar las excepciones y lanzarlas nosotros y crear excepciones propias para ellos
tenemos que haber dado las clases
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"

#por ejemplo, si queremos dividir 2/0 nos da un error que no nos deja de continuar el codigo,
#eso es una excepcion
#print(2/0)
#y nos da los siguiente:
#Traceback (most recent call last):
#  File "excepciones.py", line 19, in <module>
#   print(2/0)
#ZeroDivisionError: division by zero

#Introduccion a raise



#video 23 de exepciones de pildorasinformaticas 

def evaluaEdad(edad):

	if edad<0:
		raise ZeroDivisionError("No se permiten edades negativas") #esto nos produce un error que luego hay que capturar
	if edad<20:
		return "eres muy joven"
	if edad<40:
		return "eres joven"
	if edad<65:
		return "eres maduro"
	if edad<100:
		return "Cuídate..."

try:
	print(evaluaEdad(-15)) # con lo que esto nos da un error
# pero de esta forma el error no lo conoce porque no está definido
except ZeroDivisionError as e:
	print("El error es", e)
print("Y el programa termina aquí")



