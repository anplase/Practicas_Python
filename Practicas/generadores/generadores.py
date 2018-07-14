#generador es para crear objetos sin necesidad de memoria para dicho objeto
#def generador(*args):
#	for valor in args:
#		return valor*10 #esto devolveria el valor por 10 pero como un entero 
#						#no es iterable pues no funcionaria
#for valor in generador(1,2,3,4,5,6,7,8,9):
#	print(valor)

def generador(*args):
	for valor in args:
		yield valor*10   #esta palabra yield es la importante de los generadores porque es la
						#la que produce el generadores
for valor in generador(1,2,3,4,5,6,7,8,9):
	print(valor)

print("solo que aquí se ha hecho que nos de una lista y el for la recorre al final entera")
print()



"""pero para que entendamos mejor un generador es una función que nos va a ir generando unos
pero en vez de crear una lista con los valores, se va creando uno a uno y va mostrando uno a uno
cuando se necesite, y así no ocupa todo el espacio en memoria que necesita la lista, solo la del
un solo valor, y por otro lado no tenemos que crear la lista cada vez que necesitemos un solo valor
con todo esto hacemos lo siguiente
"""
 
def generador(limite):
	"""Este generador me va a generar diez numeros pares pero nos va a general de uno en uno 
	para que cuando se vaya a usar me de el que necesito nada más y no ocupar espacio."""
	num=1
	while num<limite:
		yield num*2 #el yield es el que se encarga de fabricar el generador a diferencia de cualquier 
					# otra funcion que es el return
		num+=1
damepares=generador(10)
print("Aquí empezamos con un generador de pares")
print(next(damepares))  #con el next pedimos el siguiente valor del generador
print("Aquí se hace otro proceso")
print(next(damepares))
print("Aquí realizamos un segundo proceso")

print()
print("también está el yield from que es cuando se va a dar valores de una matriz de dos dimensiones")
print(" que es que cuando tenemos que dar por ejemplo ciudades y dentro de los nombre las letras")
print("este generador tiene dos dimensiones, una la de los nombres y la otra las letras de los nombres")
print("y ello nos lo da el yield from u otro for dentro anidado, pero el yield from nos lo soluciona")
print("como generador ")

def busca_ciudades(*ciudades):
	for elemento in ciudades:
		yield elemento
letras_ciudades=busca_ciudades("Madrid","Barcelona","Valencia")
print(next(letras_ciudades))# solo va a dar dos ciudades en los dos print()
print(next(letras_ciudades))
#de esta forma nos da las dos ciudades.
print()

def busca_ciudades2(*ciudades):
	for letras_ciudades_españolas in ciudades:
		for elemento in letras_ciudades_españolas:
			yield elemento
letras_ciudades2=busca_ciudades2("Madrid","Barcelona","Valencia")
print(next(letras_ciudades2))# solo va a dar dos ciudades en los dos print()
print(next(letras_ciudades2))
#pero claro esto nos da las dos primeras letras del primer nombre pero hemos tenido que realizar
#un for anidado.

print()
print("el siguiente generador hace lo mismo pero con un solo for")

def busca_ciudades3(*ciudades):
	for letras_ciudades_españolas in ciudades:
		#for elemento in letras_ciudades_españolas:
			yield from letras_ciudades_españolas
letras_ciudades2=busca_ciudades2("Madrid","Barcelona","Valencia")
print(next(letras_ciudades2))# solo va a dar dos ciudades en los dos print()
print(next(letras_ciudades2))




