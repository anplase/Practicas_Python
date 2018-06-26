lista = list ('antonio')
print (lista)

for letra in lista:  #esto va recorriendo la lista y asignandoles a letra cada valor de la lista
	print ('letra es: {}'.format(letra)) 

print ('')
print ('esto de ahora es sabiendo el indice con i que voy aumentando en cada iteración')
i=-1
for letra in lista:  #esto va recorriendo la lista y asignandoles a letra cada valor de la lista
	i=i+1	# de paso voy tomando la posición en cada iteración con i
	print ('letra es: {} y en la posición: {}'.format(letra, i)) 

print ('')
print ('esto de ahora es con: for indice, letra in enumerate(lista)')
for indice, letra in enumerate(lista):  #esto va recorriendo la lista y asignandoles a letra cada valor de la lista
	print ('letra es: {} y la posición con enumerate(lista) es:{}'.format(letra, indice)) 


array = [lista[:], lista[:]]
print ('array es:',array)
print ('array = [lista[:], lista[:]] asi no funciona')

for i in lista:
	for x in lista:
		print ('[',i,']','  ','[',x,']')

array2= [lista[:], [c.upper() for c in lista]]
print ('array 2 de  array2= [lista[:], [c.upper() for c in lista]] es', array2)


print(' ')
print('empieza con ordenación')
frase = 'hola me llamo antonio'
numeros = [1,2,3,5,6,8,7,9,4]

palabras=frase.split() #convierto la frase en una lista de palabras con split
print('muestro las palabras sin ordenar:')
print('{}'.format(palabras))
print('muestro los numeros sin ordenar:')
print('{}'.format(numeros))
print('')
palabras.sort()
numeros.sort()
print('muestro los numeros y las palabras ordenadas')
print('{}'.format(palabras))
print(numeros)