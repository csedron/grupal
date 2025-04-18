# Programa para convertir un número binario a decimal
# con validación de entrada

# Pedimos al usuario que ingrese un número binario
binario = input("Ingresá un número binario (ej: 1010): ")

# Verificamos que el número ingresado solo contenga 0 y 1
while not all(digito in '01' for digito in binario):
    # Si no es válido, mostramos un mensaje de error
    print("Error: El número ingresado no es un número binario válido (solo debe contener 0 y 1).")
    # Pedimos nuevamente el número binario
    binario = input("Ingresá un número binario válido (por ejemplo, 1010): ")

# Si la entrada es válida, convertimos a decimal
decimal = int (binario, 2)
print(f"El número binario {binario} en decimal es: {decimal}")
