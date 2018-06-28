def suma(valor_uno, valor_dos):
	return(valor_uno+valor_dos)

resultado=suma(10,20)
print(resultado)

#lambdas nos crea funciones anónimas
print()
mi_funcion=suma   #esto se hace cuando se reunan unas condiciones
resultado=mi_funcion(20,10)
print(resultado)

print()
mi_funcion_lambda = lambda valor_uno, valor_dos : valor_uno+valor_dos
#después de la palabra reservado lambdas se ponen los argumentos ydespués de los dos 
#puntos se colocan que queramos ejecutar y en una sola linea, no utilizar ciclos ni 
#condicionales, no se coloca la parabra return porque las lambdas regresan siempre algo
# con lo que no hace falta hacer lo de arriba para obtener un mismo resultado
resultado=mi_funcion_lambda(10,20)
print(resultado)

print()
print("otra de ejemplo")
formato = lambda sentencia: "¿{}?".format(sentencia)
resultado = formato("puedes hacer de esto una pregunta")
print(resultado)

print()
print("otra de ejemplo")
formato = lambda sentencia, sentencia2: "¿{}?, ¿{}?".format(sentencia, sentencia2)
resultado = formato("puedes hacer de esto una pregunta", "y otra")
print(resultado)

print()
print("otra lambda pero sin valor")
no_valor = lambda : 10  #las lambdas pueden no recibir argumentos
resultado = no_valor()
print(resultado)

print()
no_resultado = lambda : print("si no da resultado o no realiza ninguna acción daría un error por eso se poner por lo menos el print")
resultado=no_resultado()
print(resultado)