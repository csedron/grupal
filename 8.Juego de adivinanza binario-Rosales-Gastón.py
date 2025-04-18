################################# ENUNCIADO #################################

# 8 - Juego de Adivinanza en Binario:
#Muestren un número en binario y desafíen al usuario a adivinar su equivalente decimal
#, o viceversa, reforzando la conversión entre ambos sistemas

import random

## FUNCIONES

def convertir_a_binario(cociente):
    #defino una variable donde se almacenará el resto
    resto=''
        #mientras el numero ingresado(cociente) sea mayor que 0 el ciclo se ejecutará y almacena el resultado en Resto
    while cociente > 0:
        #en la variable resto, agrego el resto de los resultados del cociente%2
        resto += str(cociente%2)
        #decrecemos la variable cociente para que el ciclo While finalice
        cociente = cociente//2
        #utilizo el ::-1 para revertir la cadena y la conversion a binario sea correcta
    return int(resto[::-1])


#funcion para determinar un numero random por default entre 1 y 15 valiendonos de la herramienta importada 'random'
def entero_random(min=1, max=15):
    numero = random.randint(min, max)
    return numero


def convertir_decimal(num):
    #definimos suma para almacenar el resultado en base decimal
    #e indice para ir recorriendo el numero
    suma=0
    indice=0
    # Mientras el número binario (en formato decimal) sea mayor o igual a 1
    while num>=1:
        # Obtenemos el último dígito del número binario
        digito=num%10
        # Eliminamos el último dígito dividiendo entre 10 y convirtiendo a entero
        num=int(num/10)
        # Sumamos el valor decimal del dígito según su posición (2^indice)
        suma=suma+digito*pow(2, indice)
        # Incrementamos el índice para pasar a la siguiente potencia de 2
        indice+=1
    return suma


### FUNCION PRINCIPAL

#Establecemos un numero random y lo convertimos a base binaria
numOcultoBinario = convertir_a_binario(entero_random())

#Esta variable capta un numero entero
numUsuario = int(input(f'Ingrese el valor decimal correspondiente a {numOcultoBinario} o ingrese * para salir:  '))
print(f'PISTA. El numero a descubrir tiene esta entre 1 y 15')


#Este ciclo se ejecutara mientras el usuario no adivine(haga que ambas variables se igualen) o presione *
while numOcultoBinario!=convertir_a_binario(numUsuario) or numUsuario != '*':
    if numOcultoBinario != convertir_a_binario(numUsuario):
        #Si el numero ingresado es diferente al dado por el algoritmo, se solicitara nuevamente.
        numUsuario = int(input(f'INCORRECTO :( .Ingrese nuevamente el decimal correspondiente a {numOcultoBinario} o ingrese * para salir:  '))
    else:
        print('Perfecto! Acertaste')
        break

print('¡Ganaste el juego!')
print(f'El numero binario: {numOcultoBinario} es equivalente a {numUsuario} en decimal.')
