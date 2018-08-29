#!/usr/bin/python3    

"""
Vamos a ver los menús y submenús.

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

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300) 	#hemos creado una barra menu principal 
													#y a ella se le agregarán los submenus

archivoMenu=Menu(barraMenu, tearoff=0) #primer submenu, archivos
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator() #Añade un separador
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu, tearoff=0) #para quitar las lineas que salen que se llaman lagrimas
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu)
archivoHerramientas.add_command(label="Herramientas")
archivoHerramientas.add_command(label="Tijeras")
archivoHerramientas.add_command(label="Alicates")
archivoHerramientas.add_command(label="Jejeje")

archivoAyuda=Menu(barraMenu)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edición", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)




mainloop()

