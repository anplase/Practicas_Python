#!/usr/bin/python3    

"""
Aquí vamos a practicar con algunas librerias
"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


import random   #esto nos da numeros aleatorios, por ejemplo

valor= random.randint(0,10) #esto nos devuelve numeros entre el 0 y el 10 incluidos los dos
print(valor)

lista = [True, "string", 23, False]
valor = random.choice(lista) #esto no da valores de la lista a su libre albedrio
print(valor)

#si queremos desordenar una lista por ejemplo
print("antes de desordenar la lista:",lista)
random.shuffle(lista)
print("despues de desordenar la lista:",lista)

print()

import datetime
print(datetime.datetime.now()) #esto nos da la fecha y hora de ahora.

print()

import sys 	#para trabajar con algunas funciones de nuestro sistema
#vamos a hacer una barra de progreso por ejemplo y para ello necesitamos un for
import time	#esto es para colocar un delay para que espere un momento y nos de tiempo ver el progreso

for i in range(100):
	time.sleep(0.03)	#en segundos
	sys.stdout.write("Texto")
	sys.stdout.flush()

print()
#como el texto no nos ayuda pues se hace lo siguiente
for i in range(100):
	time.sleep(0.08)	#en segundos
	sys.stdout.write("\r%d" %i)  #imprime en la misma posición, con \r y se imprime el valor i
	sys.stdout.flush()

print()
#como en principio estamos contando, pero no en función de un progreso de algo
for i in range(100):
	time.sleep(0.1)	#en segundos
	sys.stdout.write("\r%d %%" %i)  #imprime en la misma posición, con \r y se imprime el valor i
									# ahora le colocamos el % pero lo tenemos que hacer con %%
	sys.stdout.flush()

#podemos ver la documentacion adjunta de 28.curso de python librerias en codigo facilito
