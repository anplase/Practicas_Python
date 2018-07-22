#!/usr/bin/python3    

"""
herencia multiple, vamos a probar como utilizarla función super()
ello lo que hace es simular o llamar a la clase padre de la clase donde la instamos

"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


class Mundo():
	def __init__(self, continente):
		print("el mundo es redondo y el continente es: ", self.continente)

class Persona(Mundo):
	def __init__(self, nombre, continente):
		super().__init__(continente)
		print("entramos en la clase persona")
		self.nombre=nombre

class Nino(Persona):
	def __init__(self, edad, nombre, continente):
		super().__init__(nombre, continente)
		self.edad=edad
		print("edad: ",self.edad, "\nNombre: ", self.nombre, "y el continente:", self.continente)

Erica=Nino(35, "Erica", "Europa")


""" Todavia no se porqué no puedo hacer más de una llamada a padres, es decir utilizar en cascada
para arriba el metodo super().......