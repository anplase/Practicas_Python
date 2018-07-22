from calculadora import __name__ as __name__calculadora__
print(__name__) #aqui tenemos el nombre de main que es siempre el que ejecuta sea su nombre el que sea, no necesariamente tiene que ser su nombre main para que nos de como resultado main.
print(__name__calculadora__) #aqui vemos como hemos importado el nombre de calculadora

if __name__=="__main__": #Es este el script principal?
	print("hola")
#esto se hace porque cuando tenemos funciones o algo en la primera identación o sea en el primer nivel
#cuando importamos calculadora, aoutmaticamente se ejecuta todo lo que haya en el primer nivel
#y para que no se ejecute, en el archivo calculadora.py que se importa, se pone:
# if __name__=="__main__":  para comprobar que este script no es el principal con lo que 
# no se debe de ejecutar porque es un import el que ha llamado a dicho archivo.py
# es decir que las funciones no se ejecutarán cuando se haga un import, sino que se ejecutarán 
#cuando esté como llamadas en el main.py

"""
el valor de __name__ siempre es main, es decir, que si ejecutamos es cualquier archivo.py
print(__name__)   nos va a dar main, pero cuando se hace una llamada a otro modulo solo
para obtener alguna función, necesitamos que el nombre de dicho modulo que importamos no se
main, sino el nombre de dicho modulo, y como lo solemos importar al script donde lo llamamos
y este es el que realiza la llamada, pues si queremos que el nuestro sea el main.
""" 
from calculadora import saluda
saluda() #hemos importado saluda de calculadora.py