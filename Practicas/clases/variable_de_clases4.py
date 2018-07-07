#!/usr/bin/python3    

"""
Vamos a practicar las variables de clases, las variables de clases se pueden modificar 
a lo largo del programa, pero como norma, se usa un guion bajo delante de la variable de clase
que no se quiera que se cambie. Los programadores saben que si se encuentran una variable
con un guion bajo no la deben de cambiar

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
	
	"""Aquí vamos a practicar las variables de clase"""
	_pi = 3.1416	#la variable de clase está fuera de los metodos, y es de la clase.
					#los desarrolladores utilizan el guion bajo como convección para saber que 
					#no se debe de cambiar dicha variable. Porque esta variable no es inmutable 
					#es decir que se puede cambiar, aunque no se deba.	
	def __init__(self, radio):
		self.radio = radio

	def area(self):
		print("El area es:")
		return self.radio*self.radio*Circulo.pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(circulo_uno.radio)
print(circulo_dos.radio)
print(circulo_uno.pi)
print(Circulo.pi) 	# no  necesito crear una instancia a un objeto para poder ver lvariable de clase
					#ya que la variable no es de la instancia sino del objeto.
					#esto es loque se llama variable de clase.
print()
#como podemos saber cuando una variable es de clase o no?
print(circulo_uno.__dict__) #__dict__ nos da unas propiedados de clases, nos da las variables 
							#y nos dice como son
print()
print(circulo_uno.area())
