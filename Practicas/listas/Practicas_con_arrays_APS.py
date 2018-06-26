'''Practicas con arrys'''
print ('hola')
columnas = list('123456789')
filas = list('abcdefghi')
print(columnas)

print('i y j que creo que son i las columnas y j las filas')
for i in filas:
	print ('{} en {}' .format(i,columnas))
	for j in columnas:
			print('{}'.format(j))

