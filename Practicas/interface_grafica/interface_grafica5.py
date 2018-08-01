
"""
Vamos a probar las interface graficas, es decir las GUI en ingles.
hemos instalado primero con apt-get install python-tk

Aquí practicaremos con los widgets Text y Button


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

miNombre=StringVar() #esto lo que hace es definir la variable miNombre como string


cuadroNombre=Entry(miFrame, textvariable=miNombre)	#esto crea una entrada de texto o cuadro de texto
							#el textvariable, lo que hace es escribir en el cuadro 
							#lo que haya en la variable miNombre 
cuadroNombre.grid(row=0,column=1, padx=10, pady=10)	#el grid crea una red con filas y columnas para posicionar

nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=0, column=0, padx=10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1)
cuadroPass.config(show="*")

passLabel=Label(miFrame, text="Password")
passLabel.grid(row=1, column=0, sticky="w")

cuadroApellidos=Entry(miFrame)
cuadroApellidos.grid(row=2,column=1, padx=10, pady=10)

apellidosLabel=Label(miFrame, text="Apellidos")
apellidosLabel.grid(row=2, column=0, padx=10, pady=10)


cuadroDireccion=Entry(miFrame, width=16)
cuadroDireccion.grid(row=3,column=1, padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección")
direccionLabel.grid(row=3, column=0, padx=10, pady=10)




#para crear un cuadro de texto como de comentarios, es decir mas de una linea

cuadroComentarios=Text(miFrame, width=20, height=15)
cuadroComentarios.grid(row=4,column=1, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios")
comentariosLabel.grid(row=4, column=0, padx=10, pady=10)




#la barra de scroll hay que agregar la manualmente

scrollVert=Scrollbar(miFrame, command=cuadroComentarios.yview) #pero esto al final solo no 
				# nos coloca el scroll en su sitio y necesitamos un grid

scrollVert.grid(row=4, column=2, sticky="nsew")	#con esto el scroll se debe de adaptar, con lo que...
									# el sticky="nsew" lo que hace es estirar el scroll a lo largo 
									#del cuadro de texto comentario

cuadroComentarios.config(yscrollcommand=scrollVert.set) # esto hace que funcione el ascensor del scroll
									#correctamente, 
#Es decir que necesitamos las tres lineas para crear el scroll vertical

#para agregar un boton

def codigoBoton(): #esta se ejecuta cuando cuando se pulsa el boton enviar
	miNombre.set("Antonio") #con set escribimos y con get obtenemos o leemos

botonEnvio=Button(root, text="Enviar", command=codigoBoton) #cuando se pulsa, ejecuta la función

botonEnvio.pack()





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

