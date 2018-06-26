#bucle for

# tuplas, diccionarios, listas y string son los objetos iterables

lista=[1,2,3,4,5,6,7,8,9,10]

for valor in lista: # como lista es iterable se va cambiando de valor solo
	print(valor)

nuevo_rango = range(10,20) #en un rango de 10 al 20 pero el veinte no lo imprime.
for valor in nuevo_rango:   #el primero si lo imprime pero el último no
	print(valor)
#en otros lenguajes son for valor=0; valor<20; valor +4     mas o menos


nuevo_rango = range(10,30,2) #en un rango de 10 al 30 de dos en dos
for valor in nuevo_rango:   #el primero si lo imprime pero el último no
	print(valor)


indice=0
for valor in lista:
	print(valor, 'tiene el indice', indice)
	indice +=1

indice=0
for indice, valor in enumerate(lista):  #de esta forma sabemos el indice con enumerate
	print(valor, 'tiene el indice', indice)
	

for valor in range(0,len(lista)): #con len() me da la longitud de la lista
	print(valor)

for valor in 'Curso de codigo':  #iterando string
	print(valor)

diccionario={'a':10, 'b':20, 'c':500}
for llave, valor in diccionario.items():  #el item de un diccionario nos da lo mismo que enumerate de una lista los dos valores
	print('la llave', llave, 'tiene el valor de ',valor)
	