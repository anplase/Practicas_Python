# Aquí practicaremos las funciones

# si tenemos por ejemplo:


def factorial_numero(): #la nomenclaura de nombre tiene que ser así, con guion bajo para separar
	numero=5
	factorial=1
	while numero>0:
		factorial= factorial*numero
		numero-=1
	pass
	print(factorial)
	pass

factorial_numero() #como no nos develve nada pues solo ejecutamos la función


#ahora le vamos a pasar el argumentos a la función
def factorial_numero(numero): #la nomenclaura de nombre tiene que ser así, con guion bajo para separar
	factorial=1
	while numero>0:
		factorial= factorial*numero
		numero-=1

	pass
	return factorial
	pass
print(factorial_numero(4)) #aquí le pasamos un valor a la función y como nos devuelve por return
# pues lo imprimo directamente sin crear ninguna variable

def suma(x,y):
	resultado=x+y
	return resultado
print(suma(2,3))

def suma(x,y):  #la x y la y son variables locales
	resultado=x+y
	return resultado,x, y
print('nos devuleve la suma ',suma(2,3),' y luego los dos valores que se le da')
lista=suma(2,3)
print('imprimo solo los dos valores que le doy despues de haber pasa por la función', lista[1:3])

# Pasamos a una funcion otra funcion
print()
print('pasamos a una función otra, y a una variable')
def resta(x,y):
	return x-y
def mostrar_resultado(funcion):
	print(funcion(5,3))

funci_prueba=resta
mostrar_resultado(funci_prueba)





print()
#CUANDO NO SE SABE QUE CAMTIDAD DE ARGUMENTOS SE LE PASA A UNA FUNCIÓN
def suma_argumentos_desconocidos(*args): #se llama args como convección de todo los programadores
	print(args)
	# al final convierte args en una tuple
	print(type(args)) # nos dice el tipo y podemos ver como es tupla
	result=0
	for valor in args:
		result=result+valor
	return result


resultado= suma_argumentos_desconocidos(3, 4, 5)
print(resultado)




print()
#de la misma forma que se toma como convección el nuemro de argumentos como *args y nos lo muestra como
# una tupla, ahora lo hacemos pero lo que nos muestra es un diccionario
def diccionario_resta(**kwargs):
	valor=kwargs.get("valor", "no contiene el valor")
	print(valor)

resultado= diccionario_resta(a="Eduardo", x=2, y=9, z=True)
print(resultado)



#   * -> un asterisco es  n valores para nuestra función y se convierten en Tuplas
#   ** -> dos asteriscos  n valores para nuestra función y se convierte en diccionarios











