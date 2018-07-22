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


class Persona():
	
	def __init__(self, nombre, edad, residencia):
	
		self.nombre=nombre
	
		self.edad=edad
	
		self.residencia=residencia



	def descripcion(self):

		print("Nombre: ",self.nombre, "\nEdad: ",self.edad, "\nResidencia: ", self.residencia)



class Empleado(Persona): #esta clase de Empleado hereda de la clase Persona

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)	#Aquí llamamos a la
			#clase superior y de esta al metodo __init__ y le pasamos como variables los argumentos
			# con ello podemos llamar al constructor de la clase padr desde la clase hija

		self.salario=salario

		self.antigüedad=antigüedad


	def descripcion(self):

		super().descripcion()	#Llamamos al metodo descripción de la clase padre a este con el 
			# metodo super(), y luego seguimos con el metodo descripción de la clase hija

		print("Salario: ", self.salario, "\nAntigüedad: ",self.antigüedad)

Manuel=Empleado(2500, 55, "Manuel", 35, "España")
Manuel.descripcion()	#desde aquí se llama a metodo descripción de la clase Empleado
						# y esta a su ves llama al metodo descripción de la clase padre
						# Persona.
#Manuel es un tipo empleado pero nos imaginamos que no lo sabemos seguro, pues se utiliza el metodo
# isinstance(Nombre_instancia, clase)

print(isinstance(Manuel, Empleado))#si imprime un True nos dice que Manuel es de la clase Empleado

print(isinstance(Manuel, Persona)) # y ahora comprobamos que es de tipo Persona
#de las dos formas no dice que si son instancias de las dos clases

#vamos a probar otro para ver que nos da un False

Antonio=Persona("Antonio", 36, "España")
print("Antonio va a ser instancia de Persona pero no de Empleado:")
print("es Antonio una instancia de Empleado? ", isinstance(Antonio, Empleado))
print("es Antonio una instancia de Persona? ", isinstance(Antonio, Persona))




