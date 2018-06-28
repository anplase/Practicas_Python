#son funciones que reciben como parametros otras funciones

def validacion(num_uno, num_dos):
 	return num_uno>0 and num_dos>0

def division (num_uno, num_dos):
 	if validacion(num_uno,num_dos):  #se llama a otra función y recordemos que el print es otra función
 		return num_uno/num_dos

resultado=division(10,0)
print(resultado)
print("se obtiene un None porque es entre 0")
print("si ponemos otro valor que no sea 0 se realiza la divisón corrrectamente")
print("pero es una prueba")
#que pasaria si la función validación solo la va a uasr división?
# pues se haría anidada dentro de la función división

print()
def division2(num_uno, num_dos):
	def validacion2():  #no hace falta pasarle los parametro porque el num_uno y num_dos que se 
						#define en la función principal ya se pasan interna a dicha función
						#y se utiliza en las demás funciones o bucles
		return num_uno>0 and num_dos>0
	if validacion2():
		return num_uno/num_dos

resultado= division2(10,0)
print(resultado)



