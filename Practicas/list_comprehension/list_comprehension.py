"""
lista = []
for valor in range (0,101):
	lista.append(valor)

print(lista)

De esta forma se puede crear un lista con 100 elementos, pero como lo que queremos ver es
las list comprehension, pues se hará de la siguiente forma.

Las list comprehension son colocar en una sola linea varias sentencias

"""

lista=[ valor for valor in range(0,101) ] # creamos una lista con 100 valores
print(lista)

lista=[ 'hola' for valor in range(0,101) ] #creamos una lista de 100 elementos con hola como valor cada elemento
print(lista)

#reglas de las list comprehension
#1- valor a agregar a la lista, en esta ultima es 'hola'
#2- un ciclo, en este caso es un for
# variable = valoraagregar unciclo

#aquí vemos una lista de 0 a 100 con valores pares porque son divisibles por dos y el módulo
#o resto da 0
lista=[ valor for valor in range(0,101) if valor %2 == 0 ]
print()
print('Esto es una lista:')
print(lista)

tupla=tuple(valor for valor in range(0,101) if valor %2 != 0) # ahora son lo impares y en una tupla
print()
print('Esto es una tupla:')
print(tupla)

diccionario={ indice:valor  for indice, valor in enumerate(lista) }
print()
print('Esto es un diccionario:')
print(diccionario)


diccionario={ indice:valor  for indice, valor in enumerate(lista) if indice<10}
print()
print('Esto es un diccionario recortado a indice de 10:')
print(diccionario)