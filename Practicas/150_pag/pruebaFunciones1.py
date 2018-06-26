print ('hola')

def suma(uno, dos):
	sumadedos = uno + dos
	return sumadedos, uno, dos	
resta=suma(3, 4)
print (resta[2])
print (type(resta))	#vemos como al devolver la 
					#mas de un valor lo convierte en 
					#tupla