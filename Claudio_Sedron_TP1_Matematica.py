# Simulador de Sumador de 1 Bit:
# Programen un sumador simple que utilice lógica booleana para sumar dos dígitos binarios, 
# mostrando tanto el bit de suma como el "carry" (acarreo).

# Funcion para validar ingreso datos
def validacion_ingreso(mensaje, numero1, numero2):
    n = int(input(f"{mensaje}: "))
    while n < numero1 or n > numero2:
        n = int(input(f"{mensaje}: "))
    return n

# Funcion para sumar bits
def suma_bits(numero1, numero2):
    suma = numero1 ^ numero2 # uso de XOR
    acarreo = numero1 & numero2 # uso de AND
    return suma, acarreo

# Programa principal
numero1 = validacion_ingreso("Ingrese primer numero: ", 0, 1)
numero2 = validacion_ingreso("Ingrese segundo numero: ", 0, 1)
operacion = suma_bits(numero1, numero2)
suma = operacion[0]
acarreo = operacion[1]
print(f"El resultado de la sumatoria de los dos bits ingresados es: {suma} con un acarreo de {acarreo}")
