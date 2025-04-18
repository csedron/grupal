#Ejercicio: Desarrollar un programa que convierta números decimales a binarios

#Se solcita al usuario que ingrese un número decimal para hacerle la conversión a binario 
num_decimal = int(input("Ingrese un número decimal para convertirlo en binario: "))
num = abs(num_decimal)
#Inicializo la variable binario como vacía para luego poder ingresar datos
binario = ""

#Ejecuto el ciclo while con la condición lógica p/que corte cuando la división entera por 2 del númeo ingresada sea > 0
while num > 0:
    resto = num % 2 #Devuelve el resto de la división
    binario = str(resto) + binario
    num = num // 2

#Se muestra por pantalla el número binario equivalente al núm decimal ingresado
print(f"El número binario es: {binario}")