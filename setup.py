from setuptools import setup

setup(

	name="paquetecalculadora",
	version="1.0",
	descrption="Paquete de calculadora",
	author="Antonio",
	author_email="anplase2@hotmail.com",
	url="www.prueba_aps.com",
	packages=["Practicas","Practicas.paquetes","Practicas.paquetes.paquete_cal"]

# Una parte importante es el dato packages, que lo que hace es derireccionar
# segun donde metamos el archivo setup.py que debe de estar en el raiz de python
# y el archivo a realizar el modulo que tenemos que ir carpeta a carpeta, por
#eso la primera carpeta es Practicas, la segunda paquetes despues el archivo
#pongo el setup.py en la carpeta de python que la tengo dentro de programación
#escribimos esto en la consola desde el directorio donde está el setup.py
#python setup.py sdist
#esto nos genera dos carpetas-info y otra dist






	)