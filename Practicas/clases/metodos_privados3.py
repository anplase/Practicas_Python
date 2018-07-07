#!/usr/bin/python3    

"""
Aquí vamos a practicar los metodos privados, esto nos sirve para:
los atributos privados solo son modificados por la clase y no por la instancia

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
	""" Creamos un ususario para dar su username, password, email y practicamos los atributos
	y metodos privados
	"""
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

antonio = Usuario("antonio", "antonio123", "anplase2@hotmail.com") #esta es mi instancia a la clase
print(antonio.username)
print(antonio.password)
print(antonio.email)

# si nosotros queremos insetar un algoritmo para que el password se encripte hacemos lo siguiente
print()

class Usuario2:
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password) #el doble guión bajo es para hacer 
															#un atributo privado
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	def get_password(self):	#Los metodos privados tienen el metodo get y otro que no sé aún metodo ....
		return self.__password


antonio = Usuario2("antonia", "antonio123", "anplase2@hotmail.com") #esta es mi instancia a la clase
print(antonio.username)
antonio.__password = "aqui cambio el password" 	#aquí funciona el atributo privado porque habrá
												#alguna forma de llamarlo especial
print(antonio.__password)
print(antonio.email)
print(antonio.get_password())

