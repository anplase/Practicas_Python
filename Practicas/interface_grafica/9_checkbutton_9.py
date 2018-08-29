#!/usr/bin/python3    

"""
Vamos a probar los Checkbutton
A diferencia con los Radiobutton solo se puede elegir uno de ellos, en este caso los
CheckButton puede elegir varios de ellos.

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

root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opcionesViajes():
	opcionEscogida=""  #Aqui se va a almacenar las opciones que se han escogido

	if (playa.get()==1):
		opcionEscogida+=" playa"

	if (montana.get()==1):
		opcionEscogida+=" montana"

	if (turismoRural.get()==1):
		opcionEscogida+=" turismo Rural"	

	textoFinal.config(text="La opcion escogida: "+opcionEscogida)

#foto=PhotoImage(file="avion.png") #Esta opcion esta comentada porque la imagen se 
									#me sale porque es muy grande 
#Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige distinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViajes).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViajes).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViajes).pack()
# donde está, el texto del Chekbutton, se crea una variable que la llamamos playa, y 
#se le asigna el valor 1 cuando se activa o seleccionado con onvalue y con offvalue es el valor 
# cuando no esta seleccionada, y con el comando command es como se llama a otras funciones

textoFinal=Label(frame)
textoFinal.pack()

mainloop()