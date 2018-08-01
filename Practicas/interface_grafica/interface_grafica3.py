#!/usr/bin/python3    

"""
Vamos a probar las interface graficas, es decir las GUI en ingles.
hemos instalado primero con apt-get install python-tk

Aquí practicaremos con los label


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

root.title("practicas de label")

miFrame=Frame(root, width=500, height=400)
miFrame.pack()
#-----------------------------------------------------------------------------------------
"""vamos a probar los label, que son para colocar texto en la pantalla o imagenes.
para ellos se utiliza 
variableLAbel=Label(contenedor, opciones)
y las opciones pueden ser:
Text    	Texto que se muestra en el label
Anchor  	Controla la posición del texto su hay espacio suficiente para él (center por defecto)
Bg 			Color del fondo
Bitmap 		Mapa de bits que se mostrará como gráfico
Bd  		Grosor del borde (2 px por defecto)
Font  		Tipo de fuente
Fg  		Color de la fuente
Width  		Ancho del label en caracteres (no en píxeles)
Heigth  	Altura del label en caracteres (no en píxeles)
Image  		Muestra imagen en el label en lugar de texto
Justify  	Justificación del texto
------------------------------------------------------------------------------------------
"""
#miLabel=Label(miFrame, text="Hola")
#miLabel.pack() #una vez creado el label con pack()estaria terminado pero la ventana se ajustaria
				# al texto y no a las dimensiones que se le han dicho en miFrame, para ello se
				#usa place() en vez de pack()

#miLabel.place(x=100, y=200)

#En el caso de que miLabel no se vaya a utilizar mas se puede hacer todo en una sola linea ejemplo:
#Label(miFrame,text="hola alumnos", fg="blue", font=(28)).place(x=100,y=200)
miImagen=PhotoImage(file="imagen.jpg")
Label(miFrame, image=miImagen).place(x=150, y=250)





root.mainloop() #esta instrucción está pendiente constantemente y debe de estar siempre al final


