
"""
Vamos a probar las interface graficas, es decir las GUI en ingles.
hemos instalado primero con apt-get install python-tk

Aquí practicaremos con los Entry Que son entradas de texto


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

root.title("practicas con entry")

miFrame=Frame(root, width=1200, height=600) #esto crea un widgets o un contenedor como queramos llamarlo
miFrame.pack()		#Empaqueta el frame

cuadroNombre=Entry(miFrame)			#esto crea una entrada de texto o cuadro de texto
cuadroNombre.grid(row=0,column=1)	#el grid crea una red con filas y columnas para posicionar
cuadroNombre.config(fg="red", justify="right")

nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=0, column=0, sticky="e") #sticky es colocar el texto en el este como su fuesen
											# los puntos cardinales

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1)
cuadroPass.config(show="*") #Este show lo que muestra es siempre ** en vez de los caracteres

passLabel=Label(miFrame, text="Password")
passLabel.grid(row=1, column=0, sticky="w")


cuadroApellidos=Entry(miFrame)
cuadroApellidos.grid(row=2,column=1)

apellidosLabel=Label(miFrame, text="Apellidos")
apellidosLabel.grid(row=2, column=0, sticky="w") #sticky coloca el texto al oeste w en ingles


cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)

direccionLabel=Label(miFrame, text="Dirección de casas")
direccionLabel.grid(row=3, column=0, pady=10, padx=20) #pady es la distancia de un borde vertical en pixeles
														#padx es en horizontal




#-----------------------------------------------------------------------------------------
"""vamos a probar los Entry que son iguales a los label, que son para colocar texto 
en la pantalla o imagenes, para ellos se utiliza 
variableEntry=Entry(contenedor, opciones)
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

root.mainloop()

