numero=''
def pedir_numero():
	while True:
		try:
			numero = int(input('Dame un número del 1 al 10: '))
		except Exception as error: 	#lo de Exception as error no 
									#es necesario pero de esta 
									#forma se caza cualquier error
			print (error)
			print ('Ha habido un error que hay que depurar APS')
			pass					#pass hace que no pare aquí
		else:
			if 1<= numero <=10:
				print('El numero es:', numero)
				break
		finally:					#esto siempre se ejecuta 
									#pase o no por error
			print ('siempre se ejecuta, estamos en finally')
	return numero
numero = pedir_numero()
print(numero)
