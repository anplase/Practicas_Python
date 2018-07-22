#!/usr/bin/python3    

"""
Practicas con las clases, aquí vamos a ver a diferencia de clase.py \ncomo implementamos el metodo __init__ y para que sirve
Hemos creado una clase llamada Lapiz a la cual le tenemos que dar unos argumentos como\n Lapiz(color,contiene_borrador,Usa_grafito)
Por ejemplo Lapiz("Violeta", True, True)
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


class Lapiz():
	"""Creamos un objeto llamado Lapiz"""
	#los atributos esta vez están dentro de un metodo que se llama __init__
	# es especial, ya que va a ser el que le pase los valores a los atributos en su llamada
	# y se llama constructor, que es llamado por se los valores iniciales, por eso __init__
	
	def __init__(self, color = "Azul", contiene_borrador = False, usa_grafito = True):
		self.color = color
		self.contiene_borrador = contiene_borrador
		self.usa_grafito = usa_grafito

	#metodos son funciones dentro de una clase
	def dibujar(self):
		print("el lapiz está dibujando")

	def borrar(self):
		if self.es_valido_para_borrar():
			print("Y como contiene borrador")
			print("El lapiz puede borrar")
		else:
			print("Y como no contiene borrador")
			print("El lapiz no puede borrar")

	def es_valido_para_borrar(self):
		return self.contiene_borrador



#esto es una instancia a y su vez un objeto.
lapiz_generico = Lapiz("violeta", True, True)
print(lapiz_generico.color)
lapiz_generico.dibujar()
lapiz_generico.borrar()
