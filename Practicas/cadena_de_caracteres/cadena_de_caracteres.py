cadena='hola soy antonio hasta aquí la primera cadena'
cadena2="y aquí empieza la segunda cadena"

"""hola que tal estas?
y sirve para escribir varias filas"""

# En una función si se escribe lo siguiente es la ayuda de esta.
#def funcion():
#	"""Esta función se usa para probar la descripción
#	 o la ayuda de esta función
#	 """
#help (funcion)

print (cadena,cadena2)

print ("-----")

cadena3 = "¿Tú te inspiras en %s en cadena3?" % "C" #Devuelve ¿Tu te inspiras en C?
print (cadena3)

print ("-----")

cadena4="¿Quieres la %s %s en cadena4?" % ("pildora", "azul") #Devuelve ¿Quieres la pildora azul?
print (cadena4)

print ("-----")

cadena5="¿Quieres la %(obj)s %(color)s en cadena5?" % {"obj":"pildora", "color":"azul"} #Decuelve ¿Quieres la pildora azul?
print (cadena5)

print ("-----")

cadena6="¿Quieres la {} {} en cadena6?" .format("pildora", "azul")
print (cadena6)

print ("-----")

cadena7="¿Quieres la {1} {0} en cadena7?" .format("pildora", "azul")
print (cadena7)

print ("-----")

cadena8="¿Quieres la {obj} {color} en cadena8?" .format(obj="pildora", color="azul")
print (cadena8)
#este ultimo el recomendable en este libro
print ("-----")

"""
Pasar de mayusculas a minusculas y viceversa
"""

cadena8_mayusculas = cadena8.upper()   #cadena.upper() ponemos la variable cadena en mayusculas
print ('cadena 8 en mayusculas {}' .format(cadena8_mayusculas))
cadena8_minusculas = cadena8.lower()	#cadena.upper() ponemos la variable cadena en minusculas
print ('y ahora la paso a misnuculas {}' .format (cadena8_minusculas))

print ('ahora comprobamos la longitud de la cadena8 es:{}'.format(len(cadena8)))
# con len(cadena8) contamos la longitud que tiene la cadena8
print ("-----")
print ("-----")


""" Para contar el número de ocurencias de unos caracteres en una cadena
"""

cadena9='abcdabcabcdefgabadef'
print ('dame el caracter a buscar en la cadena: {}' .format(cadena9))
caracter=input()
print ('la cadena 9 tiene el caracter {}, {} veces' .format(caracter, cadena9.count(caracter)))
# con cadena9.count(y el caracter a buscar) contamos cuantas veces se repite el o los caracteres
# dentro de la cadena9

# para buscar en que posición de la cadena se encuentra se usa frase.index("caracter")
# y para buscar el siguiente frase.index("caracter", posición + 1)
print ('la posición del caracter {} en la cadena es la posición {}'.format(caracter, cadena9.index(caracter)))

posicion = cadena9.index (caracter) 
print("Posición n°:{}".format(posicion))

# para reemplazar caracteres en una cadena frase.replace('a', 'A')
print ("-----")

frase=cadena9.replace('ab','AB')
print ('la frase con los datos reempazados es:', frase)



