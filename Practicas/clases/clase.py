#!/usr/bin/python3    

"""
Practicas con las clases, empezando
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"

#Para crear un objeto lo primero es crear una clase.
#El nombre empieza por mayusculas de la clase, yla segunda palabra a continuación tambien, 
#por ejemplo class LapizDibujo:  en caso de crear una clase que se quiera llamar lapiz de dibujo

#creamos una clase Lapiz, y esta va a ser nuestra templates, o nuestra plantilla
class Lapiz():
	"""Creamos un objeto llamado Lapiz"""
	#los atributos de la clase lapiz son:
	color = "Amarillo"
	contiene_borrador = False
	usa_grafito = True

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
lapiz_generico = Lapiz()
print(lapiz_generico.color)
lapiz_generico.dibujar()
lapiz_generico.borrar()
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()

print()

lapiz_nuevo = Lapiz()
lapiz_nuevo.dibujar()
lapiz_nuevo.borrar()
lapiz_nuevo.color = "Azul"
print(lapiz_nuevo.color)




