#!/usr/bin/python3    

"""
Aquí se coloca todo lo que hace el modulo a que contexto corresponde.
"""
#la priemra linea se hace para que el sistema sepa que interprete puede ejecutar este script

# ahora se colocar los metadatos

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


def suma(num_uno,num_dos):
	"""Regresa un número entero el cual es el resultado de una suma"""
	return num_uno+num_dos

def resta(num_uno,num_dos):
	"""Regresa un número entero el cual es el resultado de una resta"""
	return num_uno-num_dos

def multiplicacion(num_uno,num_dos):
	"""Regresa un número entero el cual es el resultado de una multiplicacion"""
	return num_uno*num_dos

def division(num_uno,num_dos):
	"""Regresa un número entero el cual es el resultado de una division"""
	return num_uno/num_dos

"""
Esta es la estructura que tiene que tener todo modulos, y desde el interprete de python,
>>>import calculadora
>>>help(calculadora)
esto nos da todos comentarios, funciones y comentarios de funciones y informacions del modulo
>>>dir(calculadora)
esto nos da los atributos que pueden tener los comentarios o informacion de la funcion
"""
