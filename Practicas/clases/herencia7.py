#!/usr/bin/python3    

"""
La herencia no es más que declarar clases de objetos a partir de otras clases,
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


class Gato:
	@property
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El felino está cazando")
	
class Jaguar:
	@property #decoramos
	def garras_retractiles(self):
		return True

	def cazar(self):
		print("El felino está cazando")




gato = Gato()
jaguar = Jaguar()

print(gato.garras_retractiles)
print(jaguar.garras_retractiles)

#hasta ahora dos clases casi iguales con dos metodos cada una.

