"""
Vamos a probar las interface graficas, es decir las GUI en ingles.
hemos instalado primero con apt-get install python-tk

Vamos a hacer que funcione como tal al calculadora

"""

__author__="Antonio Plaza Serón"
__coyright__="Copyright 2018, Practicas de APS"
__credits__="Practicas de APS"

__license__="GPL"
__version__="1.0.1"
__maintainer__="Antonio Plaza"
__email__="anplase2@hotmail.com"
__status__="Developer"


from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

operacion=""
resultado=0


miFrame.pack()
#-----------pantalla-----------------------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4) #columnspan lo que hace es decir 
			#que la fila 1 va a utilizar cuatro columnas como si el texto se mezclara en las 
			#cuatro columnas que son lo que ocupa los cuatro botones inferiores
pantalla.config(background="black", fg="#03f943", justify="right")


#-----------pulsaciones teclado----------------------------------

def numeroPulsado(num):

	global operacion
	
	if operacion!="": #si operacion es diferente a cadena vacia
		
		numeroPantalla.set(num) #escribo en pantalla el numero despues de la operacion
		operacion="" #Le vuelvo a colocar cadena vacia para que vuelva a concatenar  los siguientes numeros
	
	else:
		numeroPantalla.set(numeroPantalla.get() + num)

#--------------funcion suma-------------------

def suma(num):
	global operacion
	global resultado
	resultado+=int(num) #al resultado se suma lo que hay en num, y lo que habia en num es lo que
						#habia en pantalla ante de llamar a suma
	operacion="suma"
	numeroPantalla.set(resultado)

#-----------------funcion el_resultado--------------------------

def el_resultado():

	global resultado

	numeroPantalla.set(resultado+int(numeroPantalla.get()))

	resultado=0 # esto es para que despues del igual si le doy al mas o a cualquier
				# operador no siga haciendo lo ultimo


#------------------fila 1-------------------------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)


#------------------fila 2-------------------------------------
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)


#------------------fila 3-------------------------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)



#------------------fila 2-------------------------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3)
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)


raiz.mainloop()