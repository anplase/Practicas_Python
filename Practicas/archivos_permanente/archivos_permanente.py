import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre de ", self.nombre)

	def __str__(self): #str convierte en cadena de texto un objeto
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

#se ha definido la clase de personas y nos funciona, pero como queremos que se nos guarde
#todas las personas que se vayan incluyendo, pues creamos un lista de personas que es donde
#se van a ir guardando.

class ListaPersonas:

	personas=[]







p=Persona("Sandra", "Femenino", 29)