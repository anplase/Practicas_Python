

#mi_dicionario={ 'a' : 55, 'hola':'pepe', 5:'esto es un string'}
print('Diccionario inicial')
mi_diccionario={ 'a' : 55, 'hola':'pepe', 5:'esto es un string', 2:True}
print(mi_diccionario)
print()
#los claves del diccionarios dicen que son inmutables, clave=dato, clave2=dato2

#Si utilizamos la misma clave en el diccionario, solo se crea una sola variable 
print('Diccionario con cambio varias veces a y el último valor 43')
mi_diccionario={ 'a' : 55, 'hola':'pepe', 5:'esto es un string', 2:True, 'a' : 54, 'a' : 43}
print(mi_diccionario)
print()
#clave pero solo toma el ultimo valor.

#Para asignar un nuevo valor es:   mi_diccionario[2]=False    clave=2 y valor es False
print('Diccionario con cambio del elmento 2 por False')
mi_diccionario[2]=False
print(mi_diccionario)
print() #holahola

valor=mi_diccionario.get('z',12) #donde regreso un numero, string u otra cosa
print(valor)
valor=mi_diccionario.get('z',(12,2)) #donde regreso una tupla
print(valor)
print()
#En caso de que no existe el eelmento en el diccionario que buscamos nos da un error
#para evitarlo, valor=mi_diccionario.get('a',(12,2))

print('elimino el objeto 2')
del mi_diccionario[2] 
#Para eliminar un objeto, del mi_diccionario[5] borra el elemento con clave 5

print()
llaves=mi_diccionario.keys()
print(llaves)
#para obtener solo los valores de los elemntos utilizamos.

#para poder pasarlo a una lista pura sin el dict_keys es:
print()
llaves=list(mi_diccionario.keys())
print(llaves)

#para obtener los valores por ejemplo
print()
valores=list(mi_diccionario.values())
print(valores)


#para insertar de un diccionario al otro se puede hacer mi_diccionario['z']=diccionario_dos['z']
# pero lo suyo es:
print()
diccionario_dos={'peta':34, 'ui':56}
mi_diccionario.update(diccionario_dos)
print(mi_diccionario)






