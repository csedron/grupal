
#Contador binario: Escriban un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria.

import time 

for i in range(16): #Utilizo el bucle for porque tengo un rango pre establecido. 
    time.sleep(2)   #Utilizo esta función para retardar el bucle por 2 segundos. 
    numero = (bin(i)) #Convierto a binario automaticamente con la funcion bin 
    numero_completo = format(i,"04b") #Completo con ceros a la izquierda del numero hasta 4 bits para corregir el formato. Y como la funcion bin me
                                        # devuelve un prefijo"0b", lo elimino con format(). 
    print(numero_completo)     

