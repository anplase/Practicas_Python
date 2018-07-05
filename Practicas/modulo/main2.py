from calculadora import (suma,
						resta,
						multiplicacion)
from calculadora import division as div
"""de esta forma se importa el modulo calculadora y la funcion suma, pero \nsolo dicha funcion, ventaja es que no hace falta nombrar el modulo.
y a la funcion division le hemos cambiado el nombre por div.
hay otra forma que es:
form calculadora import *    pero de esta forma importamos todd y debemos saber que es lo que tiene 
el modulo calculadora.
"""


resultado = suma(30,25)  	# no hace falta colocar calculadora.suma(30,25), sino que ya hemos importado el modulo calculadora y la funcion suma
print(resultado)
resultado2 = div(20,4)
print(resultado2)