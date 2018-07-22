#!/usr/bin/python3    

"""
Vamos a tratar los polimorfismos, quiere decir que un objeto puede cambiar de forma y a su vez 
dependiendo del contexto puede varia su funcionamiento o comportamiento, esto es cencillo ya
que el tipado es dinamico. En java esto no ocurre.
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")

#creo una instancia a la clase Moto

miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()
#Utilizamos el mismo metodo o comportamiento en los dos (desplazamiento)
#Con el Camion ocurriria lo mismo.
miVehiculo3=Camion()
#hasta aquí nada nuevo

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()	#aquí en vez de poner self, que el el supuesto nombre de la 
								#clase a la que llamamos, llamamos directamente a la clase con una
								# variable que en este caso es vehiculo 

desplazamientoVehiculo(miVehiculo)
desplazamientoVehiculo(miVehiculo2)
desplazamientoVehiculo(miVehiculo3)
#Aqui no hace falta decir de que tipo es miVehiculo 2 o 3 ya que cambia de forma según la
# variable o clase que se le asigne en la llamada
# con lo que con una función podemos llamar a una clase y ir jugando para cambiar
# el metodo o atributos etc..
#En java es mucho más dificil hacer esto ya que las variables son tipadas y no pueden cambiar
# de tipo, y a su vez utilizar el metodo Object etc....