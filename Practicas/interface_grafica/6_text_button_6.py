"""
Vamos a probar las interface graficas, es decir las GUI en ingles.
hemos instalado primero con apt-get install python-tk

Aquí practicaremos con los widgets Text y Button
Hemos creado la pantalla de una calculadora y en el siguiente capitulo
haremos que funcione omo tal


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

miFrame.pack()
#-----------pantalla-----------------------------------------

pantalla=Entry(miFrame)
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4) #columnspan lo que hace es decir 
			#que la fila 1 va a utilizar cuatro columnas como si el texto se mezclara en las 
			#cuatro columnas que son lo que ocupa los cuatro botones inferiores
pantalla.config(background="black", fg="#03f943", justify="right")


#------------------fila 1-------------------------------------
boton7=Button(miFrame, text="7", width=3)
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3)
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3)
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)


#------------------fila 2-------------------------------------
boton4=Button(miFrame, text="4", width=3)
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3)
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3)
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)


#------------------fila 3-------------------------------------
boton1=Button(miFrame, text="1", width=3)
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3)
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3)
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)



#------------------fila 2-------------------------------------
boton0=Button(miFrame, text="0", width=3)
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3)
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3)
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3)
botonSum.grid(row=5, column=4)


raiz.mainloop()