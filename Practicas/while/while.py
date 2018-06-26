
condicion=0



while condicion<10: #< <= > >= == !=
	print('lo que sea')
	print(condicion)
	condicion+=1  #esto es condicion= condicion+1
else:
	print('despues del while')

#para detener ctrl+0 en caso de que entre en un bucle cerrado

condicion=0
while condicion<10: #< <= > >= == !=
	print('lo que sea')
	print(condicion)
	condicion+=1  #esto es condicion= condicion+1
	if condicion == 5 :
		pass
		break #detenemos abruptamente el ciclo en el 5

else:
	print('despues del while')
