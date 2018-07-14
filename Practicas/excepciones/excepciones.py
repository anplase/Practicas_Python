#!/usr/bin/python3    

"""
Vamos a practicar las excepciones
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



try:
	print(2/0) #esto es lo que se va a intentar ejecutar
except:
	print("esto se ejecuta cuando falla el primer bloque")
print("Se termino el script")
#es recomendable no poner pass despues de except para debugear el programa y encontrar los errores
#pero no estaría completo, habria que colocar que tipo de except es.





print()

try:
	print(2/0) #esto es lo que se va a intentar ejecutar
except ZeroDivisionError:
	print("esto se ejecuta cuando falla el primer bloque")
	#pass no colocar para encontrar el mensaje
print("Se termino el script")

print()

try:
	print(2/0) #esto es lo que se va a intentar ejecutar
except ZeroDivisionError as ex:	# con as y variable podemos imprimir la variable y saber que ha fallado
	print(ex) 						
	print("esto se ejecuta cuando falla el primer bloque")
	#pass no colocar para encontrar el mensaje
print("Se termino el script")




print()
#otro ejemplo

try:
	lista = [1,2]
	print(lista[9]) #como no existe esta posicion pues nos va a dar un error
except IndexError as ex:
	print(ex)
	print("No es posible obtener el valor en 9")
except ZeroDivisionError as ex:	# con as y variable podemos imprimir la variable y saber que ha fallado
	print(ex) 						
	print("esto se ejecuta cuando falla el primer bloque")
	#pass no colocar para encontrar el mensaje
print("Se termino el script")



print()
#cuando no se que tipo de error, entonces se hace así
try:
	print(2/0) #esto es lo que se va a intentar ejecutar
except Exception as ex:	# con as y variable podemos imprimir la variable y saber que ha fallado
	print(ex) 						
	print("No se que pasó pero algo pasó")
	#pass no colocar para encontrar el mensaje
	print("Se termino el script")
#esta ultima es la generica que casi siempre se puede usar
finally:
	print("este bloque siempre se ejecuta falle o no ")
# es normal encontrar en otros codigos meter en el finally el cierra de las bases de datos
# para que no se queden abiertas





