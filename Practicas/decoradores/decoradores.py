#empezamos con decoradores
def decorador(func):  #A
	def nueva_funcion(*args, **kwargs):
		print("Vamos a ejercutar la función") #aquí por ejemplose puede abrir una base de datos
		func(*args, **kwargs) #B  #se leen los datos
		print("Se ejecutó la función") # se cierra la conexión con la base de datos
	return nueva_funcion  #C

@decorador
def saluda():  #función a decorar
	print("Hola Mundo")	
#A,B,C son funciones
#a la función A se pasa la función B para que nos devuelva la función C


@decorador
def suma(num_uno, num_dos):  #función a decorar pero esta vez pasando le parametros
	print(num_uno+num_dos)	
#A,B,C son funciones
#a la función A se pasa la función B para que nos devuelva la función C
saluda()
suma(80,17)

print()

#NUEVO DECORADOR
#esta vez creando las funciones dentro
def decorador2(func2):
	def before_action():
		print("antes de la acción")
	
	def after_action():
		print("después de la acción")
	
	def nueva_funcion2(*args, **kwargs):
		before_action()
		resultado = func2(*args, **kwargs)
		after_action()
		return resultado
	return nueva_funcion2

@decorador2
def multiplicación(x,y):
	return x*y

print(multiplicación(3,4))

print()
#NUEVO DECORADOR
#esta vez creando las funciones dentro y le pasamos datos desde el 

def conexiónTCP(puerto):

	def realizar_conexion(leer_datos):
		def abrimos_conexion():
			print("Abriendo la conexión TCP")

		def cerrando_conexion():
			print("Cerrando la conexión TCP")
		
		def conectandoTCP(*args, **kwargs):
			if puerto==502:
				print("Puerto correcto 502")
				abrimos_conexion()
			resultado = leer_datos(*args, **kwargs)
			cerrando_conexion()
			return resultado
		return conectandoTCP
	return realizar_conexion

@conexiónTCP(puerto=502)
def conexion(x,y):
	print("Leyendo datos, esta es la parte donde se leen los datos")
	return x/y

print(conexion(20,5))




