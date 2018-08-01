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

	def __init__(self):

		listaDePersonas=open("ficheroExterno", "ab+")  #ab+ es agregar información binaria
		listaDePersonas.seek(0) #desplazo el cursor al principio para que cuando se vuelva a leer sea desde el principio

		try: #como la primera vez que se intenta leer no tiene nada daria error por el el try de excepciones
			self.personas=pickle.load(listaDePersonas)
			print("Secargarón {} personas del fichero externo".format(len(self.personas)))

		except:
			print("El fichero está vacío")

		finally:
			listaDePersonas.close() #se cierra y se borra ya que ya no se va a volver a usar
			del (listaDePersonas)


	def agregarPersonas(self,p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for i in self.personas:
			print(i)


	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del (listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("La información del fichero externo es la siguiente:")
		print("Hay un total de: {} personas en el ficheroExterno".format(len(self.personas)))
		for i in self.personas:
			print(i)

	def eliminaPersonas(self):
		personaAEliminar=int(input("Dame el numero de pesona a eliminar: "))
		del personas[4]
		print("Persona eliminada")




miLista=ListaPersonas()
persona=Persona("Ana", "Femenino", 29)
miLista.agregarPersonas(persona)

bucle=True
while bucle:
	
	a=input("¿Agrego, Muestro, Elimino, Guardo y Termino? a, m, e, gt: ")
	
	if a=="a": 
		persona2=Persona("PEpa", "Feme", 34)
		miLista.agregarPersonas(persona2)
		print("Agregamos esta persona")

	elif a=="m": 
		miLista.mostrarInfoFicheroExterno()
		print("Mostramos la información")
	elif a=="e":
		miLista.eliminaPersonas()

	elif a=="gt":
		miLista.guardarPersonasEnFicheroExterno()
		print("aquí terminamos")
		bucle=False

	else:
		print("parametro no valido")



print()
print("Muestro todas las personas")
print()
miLista.mostrarInfoFicheroExterno()