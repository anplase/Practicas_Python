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

raiz.resizable(1,1) #este admite dos parametros booleanos y el primero corresponde al ancho
					#width y el segundo al alto height y lo que hace es permitir para que  
					#se pueda redimensionar. A 0 o False bloquea ese lado ya sea 
					#horizontal (ancho) o el vertical (alto)

#raiz.iconbitmap("nombre y ruta de la imagen") esto lo que hace es poner en la esquina un logo.ico

raiz.geometry("650x350") #dimensiona la ventana ancho y alto

raiz.config(bg="blue") #config hace muchas cosas, bg es background (fondo) y color 

#En windows abre dos ventanas, una la que necesitamos, y otra la de la consola detras,
#y como no queremos la forma de hacer que no salga es renombrar el fichero en windows 
#con la extención .pyw que aunque windows dice que cuiddo, no hacer caso y hacerlo


raiz.mainloop() #esta instrucción está pendiente constantemente y debe de estar siempre al final


