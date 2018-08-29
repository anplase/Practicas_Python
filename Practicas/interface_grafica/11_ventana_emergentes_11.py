#!/usr/bin/python3    

"""
Vamos a ver las ventanas emergentes

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
from tkinter import messagebox  # esto es para utilizar las ventanas emergentes ya que no
								# están por defecto en la libreria de tkinter

root=Tk()

root.title("Ventanas emergentes")

def infoAdicional():
	messagebox.showinfo("Procesador de Juan", "Procesador de texto vesion 2018")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
	# dependiendo del boton que se pulse en la ventana emergente, sale yes o no y se
	#asigna a valor y con ello luego lo pasamos al if
	if valor=="yes":
		root.destroy() #función para salir de la aplicación

def probarAskokcancel():
	valor=messagebox.askokcancel("Salir", "Probando poner botones de aceptar y cancelar")
	# Esta función no devuelve si o no, sino o True o False como booleano

def probarReintentar():
	messagebox.askretrycancel("Reintentar", "No es posibe cerrar documento bloqueado")
	# Esta función no devuelve si o no, sino o True o False como booleano

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300) 	#hemos creado una barra menu principal 
													#y a ella se le agregarán los submenus

archivoMenu=Menu(barraMenu, tearoff=0) #primer submenu, archivos
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator() #Añade un separador
archivoMenu.add_command(label="Cerrar", command=probarReintentar)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0) #para quitar las lineas que salen que se llaman lagrimas
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Herramientas")
archivoHerramientas.add_command(label="Tijeras")
archivoHerramientas.add_command(label="Alicates")
archivoHerramientas.add_command(label="Jejeje", command=probarAskokcancel)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edición", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)




mainloop()

