#!/usr/bin/python3    

"""
Vamos a probar las interface graficas, es decir las GUI en ingles.
hemos instalado primero con apt-get install python-tk

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

raiz.title("Ventana de pruebas")

#raiz.resizable(1,1) #este admite dos parametros booleanos y el primero corresponde al ancho
					#width y el segundo al alto height y lo que hace es permitir para que  
					#se pueda redimensionar. A 0 o False bloquea ese lado ya sea 
					#horizontal (ancho) o el vertical (alto)

#raiz.iconbitmap("nombre y ruta de la imagen") esto lo que hace es poner en la esquina un logo.ico

raiz.geometry("650x350") #dimensiona la ventana ancho y alto

raiz.config(bg="blue") #config hace muchas cosas, bg es background (fondo) y color 


#En windows abre dos ventanas, una la que necesitamos, y otra la de la consola detras,
#y como no queremos la forma de hacer que no salga es renombrar el fichero en windows 
#con la extención .pyw que aunque windows dice que cuiddo, no hacer caso y hacerlo

miFrame=Frame() #asignamos a la variable miFrame un Frame pero luego hay que en paquetarlo
				# y hay que meterlo dentro de la raiz y por eso hay que empaquetarlo

miFrame.pack(side="right", anchor="n") #esto por ejemplo ancla el frame dentro de la raiz arriba del todo
						# con el metodo side="top" puede ser bottom, right, left etc..
						# se pueden utilizar dos alternativas, por ejemplo con el metodo anchor.
						# anchor="n" n viene de los puntos cardinales (n,s,e,w,nw,ne,sw,se)

#miFrame.pack(fill="x") #lo que hace es estirar la parte x a todo lo largo de la ventana

#miFrame.pack(fill="y", expand="True") #para hacer lo verticalmente hay que colocar el expand

miFrame.config(bd=35) #grosor del borde 

miFrame.config(relief="groove") #Esto me dibuja un borde pero por defecto el grosor es cero
								# con lo que antes hay que decirle el grosor
								#por ejemplo otro borde es sunken

miFrame.config(bg="red") #hay que darle color y tamaño

miFrame.config(width="650", height="350") #para ajustar el tamaño del frame

miFrame.config(cursor="hand2") 	#cambiar el cursor dentro del miFrame
								# otro tipo es pirate

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







raiz.mainloop() #esta instrucción está pendiente constantemente y debe de estar siempre al final


