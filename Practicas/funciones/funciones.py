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










