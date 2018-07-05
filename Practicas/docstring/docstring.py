"""para cocumentar hay que seguir unas reglas que vamos a comentar"""


def generador(*args):
	"""Para comentar lo que hace una función se debe de hacer aquí, inmediatamente\ndespuésde declarar la función y con triples comillas, por ejemplo:\nRecibe n cantidad de número y regresa el número además de regresa\nTrue o False si el número es mayor a 5
	"""
	for valor in args:
		yield valor, True if valor >5 else False



nombre = generador.__name__
documetacion = generador.__doc__ 	#__doc__ es un atributo si se sabe algo de programación a objetos,
									#y en python las funciones son un objeto.

print("El nombre es:\n",nombre)
print("La documentación es:\n",documetacion)


"""desde el interprete de python se puede tambien obtener estos datos de la siguiente forma:

>>>from nombredelarchivo import nombrefuncion
>>>help(nombrefuncion)

ejemplo en este caso
>>>from docstring import generador
>>>help(generador)
>>>

"""