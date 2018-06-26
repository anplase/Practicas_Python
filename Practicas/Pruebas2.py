print("hola mundo")

curso = 'Curso de '
tipo = 'python'

print ('{}{}'.format(curso, tipo))

frase = input("escribe la frase:   ") #entrada por teclado
print(frase)

numerocaracteres=len(frase) # longitud de la cadena de caracteres
print(numerocaracteres)

num=frase.count('a') #cuenta los caracteres a que hay en la frase
print(num)

donde=frase.find('a')
print(donde)

if num > 0:
	print('este es el primer caracter {} que se encuentra'.format(donde))
	for i in range(1,num):
		donde = frase.find('a',donde+1)
		print('este es el valor de i= {} que encontramos'.format(i))
		print('este caracter es el {} que se ha encontrado'.format(donde))
print()
lista = ['hola', 15, 15.65, True]
print(lista)
lista.append('insertado')
print('acabo de insertar insertado con lista.append("insertado")')
print(lista)
lista.insert(1,111)
print('inserto en el lugar 1 el 111 con lista.insert(1,111)')
print(lista)