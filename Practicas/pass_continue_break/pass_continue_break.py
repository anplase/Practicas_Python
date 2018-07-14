#!/usr/bin/python3    

"""
vamos a practicar con el pass, continue y con el break
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


email=input("introduce tu email, por favor:") #aquí se pide el email y lo guarda en email
for i in email:
	if i == "@":
		arroba = True, "se ha encontrado un arroba"
		break; # este break lo que hace es terminar el for y salir
#else: # OJO!! este else no es del if, sino del for, si sale del for bruscamente, entra aquí.
	arroba = False, "NO ha encontrado un arroba"
print(arroba)

print()

for letra in "python":
	if letra=="h":
		continue 	# Aqui el continue hace que no siga ejecutando lo que continua en el if 
					#y pasa al siguiente ciclo del for
	print("Viendo la letra: " + letra)

print()
#por ejemplo, aqui vamos a contar los caracteres sin contar los espacios
nombre="Pildoras Informaticas"
contador=0
for i in nombre:
	if i==" ":
		continue
	contador+=1
print(contador)

#al crar una clase o una función se puede poner el pass
class ClassName(object):
	pass #ESTE pass se pone cuando en un futuro se añade lo que sea aqui, para no dejarla 
			# para que no de fallo se pone un pass ya que no va a dar ningun valor