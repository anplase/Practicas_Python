#!/usr/bin/python3    

"""
abrir un fichero, aqui obtenemos la ruta del archivo que se quiere abrir con la 
interface grafica, y con el print la pasamos a la consola

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
from tkinter import filedialog  # esto es para utilizar las ventanas emergentes ya que no
								# están por defecto en la libreria de tkinter

root=Tk()

root.title("Ventanas emergentes")


def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir") #esto lo que nos da es la ruta.
	print(fichero)


def abreFichero2():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="/") #esta tiene la diferencia
	# que nos da la ruta pero empieza a buscar por defecto en el raiz.
	print(fichero)


def abreFichero3():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="/", 
	filetypes=(("Ficheros de excel","*.xlsx"),("Ficheros de texto","*.txt"),("Todos los ficheros","*.*"))) #esta tiene la diferencia
	# que nos pide un tipo de archivosz en concreto o todos los tipos
	print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

Button(root, text="Abrir fichero directorio por defecto", command=abreFichero2).pack()

Button(root, text="Abrir fichero con extensiones predefinidas", command=abreFichero3).pack()

mainloop()

