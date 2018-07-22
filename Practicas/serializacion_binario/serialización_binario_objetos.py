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

class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True
	def acelerar(self):
		self.acelera=True
	def frenar(self):
		self.frena=True
	def estado(self):
		print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn marcha: ", self.enmarcha, 
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1=Vehiculo("Mazda", "MX5") #realizamos la instancia y le pasamos al constructor los dos argumentos
coche2=Vehiculo("Seat", "Ibiza")
coche3=Vehiculo("Volkswagen", "Touran")

#metemos todos los objetos cochex en una coleccion para no tener que meter todos uno por uno

coches=[coche1, coche2, coche3]

fichero=open("losCoches", "wb")

pickle.dump(coches, fichero)
# despues de todo esto, en fichero está ya guardado pero en memoria toda la información de la 
#coleccion coches, lo que ocurre que ya el de memoria no lo queremos para nada,
#lo cerramos primero y luego lo quitamos de memoria 
fichero.close()

del(fichero)

#Hasta aquí todo terminado, ya hemos generado el fichero.
#Ahora vamos a leer lo para recuperar la información.
"""-----------------------------------------------------------------------------------"""

ficheroApertura=open("losCoches", "rb")

misCoches=pickle.load(ficheroApertura)
#ya hemos cargado en la variable misCoches la información del ficheroApertura con lo que
#no nos sirve de nada y lo podemos cerrar y borrar

ficheroApertura.close()
del(ficheroApertura)

for c in misCoches:

	print(c.estado())

"""si nos llevamos la parte de las lineas para abajo a otro archivo diferente que en principio
deberia de funcionar incluyento el import pickle, no funciona, y es porque una vez que lee
el archivo guardado, no reconoce la estructura de la clase, y hay que escribir de nuevo 
la clase, con sus atributos y metodos etc..
"""



