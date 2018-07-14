#!/usr/bin/python3    

"""
Aquí vamos a ver los metodos de instancia y los metodos estaticos. Cuando un objeto realiza
acciones se llama metodos, que son funciones que se encuentran dentro de la clase.

"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"

class Circulo:
#	_pi = 3.1416 	#Variable de clase
# Esta variable de clase la hemos anulado porque la vamos a dar dese un metodo estático
#Cuando existe un metodo dentro de la clase que no tenga la palabra o arguemnto self, quiere 
# decir que es un metodo estaticos, por ejemplo.
#este metodo hay que decorarlo, por eso le añadimos un decorador. 	
	@staticmethod
	def pi():
		return 3.1416



	def __init__(self, radio):	#Metodo __init__
		self.radio = radio


#si un metodo tiene la palabra self y se encuentra dentro de la clase, es un metodo de instancia
	def area(self):				#Metodo de instancia area, que cuiere decir que un obejto puede mandar a llamarlo
		return self.radio*self.radio*self.pi()
		#o lo que es igual
		#return self.radio*self.radio*Circulo.pi()

print(Circulo.pi())

circulo_uno = Circulo(7)	#realizamos una instancia a la clase Circulo y damos como argumento el radio 7
print(circulo_uno.area())
