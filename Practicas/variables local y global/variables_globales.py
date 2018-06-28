 # Dependiendo de donde se declaren las variables serán de una forma u otra, por ejejmplo

varglobal = "hola esto es una variable global"
def prueba_variable_local():
 	varlocal="hola esto es una variable local"
 	print(varglobal, "la global")
 	print(varlocal, "la local")

prueba_variable_local()
print(varglobal)

#aunque se intente cambiar la variable global dentro de una función o bucle, fuera sigue teniendo
#el mismo valor que antes.


print()
def prueba_variable_global():
 	varglobal="la global se ha cambiado solo dentro de la función  "
 	print(varglobal)

prueba_variable_global()
print(varglobal, "NO SE HA CAMBIADO")


#PARA PODER CAMBIAR LA GLOBAL HAY QUE HACE LO SIGUIENTE, claro está refiriendonos a cambiarla
# dentro de una función, ya que fuera no se necesita nada.
print()
def prueba_variable_cambio_global():
  	global varglobal # con esto se cambia el valor de global dentro de una funcion o bucle
  	varglobal="la global SE HA CAMBIADO DEFINITIVAMENTE"

prueba_variable_cambio_global()
print(varglobal)

#las funciones pueden crear una variable global
print()
def nueva_variable_global():
	global nueva_variable
	nueva_variable="nueva variable global de dentro de una función"

nueva_variable_global()
print(nueva_variable)