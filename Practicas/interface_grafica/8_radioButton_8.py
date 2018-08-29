#!/usr/bin/python3    

"""
Vamos a probar los radiobutton


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

root=Tk()

varOption=IntVar()  #Variable de tipo entero

def imprimir():
	#print(varOption.get()) #Esto esta para que se viera en consola los recultados pero lo vamos
							#a imprimir en un text debajo de los radiobutton en la interface grafica
	if varOption.get()==1:
		etiqueta.config(text="Has elegido Masculino")
	else:
		etiqueta.config(text="Has elegido Femenino")						



Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=varOption, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOption, value=2, command=imprimir).pack()
#primero donde se encuentra, segundo el texto, donde escribe el valor cuando se pulse, que valor
# se va a escribir, y luego el comando si va a llamar a una función que en este caso es imprimir


etiqueta=Label(root) #aqui no vale poner .pack() como en Radiobutton, ya que creo que es porque
					# la asignamos a una variable
etiqueta.pack()


root.mainloop()
