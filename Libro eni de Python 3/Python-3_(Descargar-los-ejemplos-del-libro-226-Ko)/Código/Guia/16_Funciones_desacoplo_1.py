"""
Ejercicio: construir un juego "Guess The number"

PARTE 1: Pedir al usuario que introduzca un número entre 0 y 100
PARTE 2: Hacer que el usuario adivine el número

Utilizar una función para aprovechar el código común
"""

import sys

MIN = 0
MAX = 99

def pedir_numero(invitacion):
    """
    Esta función se contenta con comprobar que se obtiene un número
    """
    while True:
        # Se entra en un bucle infinito

        # Se pide un número
        entrada = input(invitacion + ": ")

        try:
            entrada = int(entrada)
        except:
            print("Solo están autorizados los caracteres [0-9].", file=sys.stderr)
        else:
            # Tenemos lo que queríamos, se sale del bucle saliendo de la función
            return entrada

def pedir_numero_limite(invitacion, minimo=MIN, maximo=MAX):
    """
    Esta función utiliza la anterior y agrega una post-condición
    sobre los límites del número a introducir
    """# Se pide un número
    invitacion = "{} entre {} y {} incluidos".format(invitacion, minimo, maximo)

    while True:
        # Se entra en un bucle infinito

        entrada = pedir_numero(invitacion)

        if minimo <= entrada <= maximo:
            # Tenemos lo que queríamos, se sale del bucle saliendo de la función
            return entrada

# PARTE 1
minimo = maximo = 0
while True:
    minimo = pedir_numero("¿Cuál es el límite inferior?")
    maximo = pedir_numero("¿Cuál es el límite superior?")
    if maximo > minimo:
        break

numero = pedir_numero_limite("Introduzca el número a adivinar", minimo, maximo)



# PARTE 2
while True:
    # Se entra en un bucle infinito
    # que permite jugar varias veces

    intento = pedir_numero_limite("Adivine el número", minimo, maximo)

    # Se comprueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
    else:
        print("¡Ha ganado!")
        break


