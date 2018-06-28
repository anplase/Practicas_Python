#con funciones para crear otras funciones
def division(num_uno, num_dos):
	def validacion():	#no hace falta pasarle los parametro porque el num_uno y num_dos que se 
						#define en la función principal ya se pasan interna a dicha función
						#y se utiliza en las demás funciones o bucles
		return num_uno>0 and num_dos>0 #esta función devuelve False o True
	return validacion  	#y la funcion principal devuelvo la función validacion que luego ella
						# devolvera (o True o False)

resultado= division(10,2)
print(resultado())
