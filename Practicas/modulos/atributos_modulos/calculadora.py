#!/usr/bin/python3    

"""
Aquí se coloca todo lo que hace el modulo a que contexto corresponde.
"""

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

def saluda():
	print("hola esto es un metodo de calculadora")

if __name__=="__main__":
	saluda()	#esto solo se ejecuta cuando la función se llame desde el main.py y no cuando 
				#se se haga el import desde main.py   porque cuando se importa automaticamente
				#se ejecuta todo el modulo.py y en este caso saluda no se ejecutará cuando se haga
				#el import en el main.py, pero si cuando se llame desde el mismo main.py
