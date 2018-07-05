#generador es para crear objetos sin necesidad de memoria para dicho objeto
#def generador(*args):
#	for valor in args:
#		return valor*10 #esto devolveria el valor por 10 pero como un entero 
#						#no es iterable pues no funcionaria
#for valor in generador(1,2,3,4,5,6,7,8,9):
#	print(valor)

def generador(*args):
	for valor in args:
		yield valor*10   #esta palabra yield es la importante de los generadores porque es la
						#la que produce el generadores
for valor in generador(1,2,3,4,5,6,7,8,9):
	print(valor)