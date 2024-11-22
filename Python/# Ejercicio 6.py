import math

# Solicitar al usuario que ingrese un número
numero = float(input("Ingresa un número: "))

# Verificar si el número es 0 o menor
if numero <= 0:
    print("Error: El número debe ser mayor que 0.")
else:
    # Calcular el cuadrado y la raíz cuadrada del número
    cuadrado = numero ** 2
    raiz_cuadrada = math.sqrt(numero)  # También se puede usar numero ** 0.5

    # Mostrar el número y sus resultados
    print(f"Del número {numero}, su cuadrado es {cuadrado} y su raíz cuadrada es {raiz_cuadrada}")
