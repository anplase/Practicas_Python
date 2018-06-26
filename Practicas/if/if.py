fruta='kiwi'

if fruta == 'kiwis' : #Si y solo si
	print('El valor es kiwi')
else:
	print('No son identicas')

#lo podemos incluir en una sola linea la condicional if
mensaje='El valor es kiwi' if fruta == 'kiwis' else 'El valor no es igual'
print(mensaje)


#Cuando queremos mas de un valor
if fruta == 'kiwis' : #Si y solo si
	print('El valor es kiwi')
elif fruta == 'manzana':
	print('es una manzana')
else:
	print('No son identicas')



#si por ejemplo
if fruta == 'kiwis' : #Si y solo si
	print('El valor es kiwis')
	pass
elif fruta == 'manzana':
	pass	 #si no se coloca el pass piensa el programa que el else iria aqui y que está mal identado
			#y si no lo lleva daría un error.
else:
	print('La fruta no es kiwi')


print()


if 0: #[],(), {}, 0, False, '', None,  son falsos todos, porque están vacios.
	print('Es verdad')

else:
	print('No es verdad')


print()
valor=0
valor2=20
if valor and valor2 == 20: #esto significa que valor no esté vacio y valor2 igual a 20
							# en el valor2 si se cumple pero en valo
							#la otra opcion es un or en vez de un and.
	print('Es verdad')
else: 
	print('No es verdad')









