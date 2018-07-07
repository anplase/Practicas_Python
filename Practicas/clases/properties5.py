#!/usr/bin/python3    

"""
Aquí vamos a practicar las properties de clases para los atributos privados
Enjava se usan los "gedes y los edesr +-"  pero python no es java con lo que se hace distinto
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


class Usuario:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password) #el doble guión bajo es para hacer 
															#un atributo privado
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	def get_password(self):	#Los metodos privados tienen el metodo get y otro que no sé aún metodo ....
		 					#Esto solo permite visualizar y no deja cambiar fuera de la clase
		return self.__password

	@property	#es como un decorador
	def password(self):
		return self.__password


antonio = Usuario("antonio", "antonio123", "anplase2@hotmail.com") #esta es mi instancia a la clase
print(antonio.password)
# si intento cambiar el passoword
#antonio.password="Nuevo password"
print(antonio.password)
# y no puedo cambiarlo


print()
#ahora vamos a intentar cambiarla de otra forma
class Usuario2:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password) #el doble guión bajo es para hacer 
															#un atributo privado
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	@property	#es como un decorador
	def password(self):
		return self.__password

	@password.setter
	def password(self, valor): #va a recoger el string que le pasemos y se lo va a asignar al atributo que le pasemos
		self.__password = self.__generar_password(valor)


antonio = Usuario2("antoni2", "antonio123", "anplase2@hotmail.com") #esta es mi instancia a la clase
print(antonio.password)
# si intento cambiar el passoword
antonio.password="Nuevo password"
print(antonio.password)
print(antonio.password)





