# Solicitar al usuario que ingrese tres números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Verificar si el primer número es negativo
if num1 < 0:
    # Calcular e imprimir el producto de los tres números
    producto = num1 * num2 * num3
    print(f"El primer número es negativo. El producto de los tres números es: {producto}")
else:
    # Calcular e imprimir la suma de los tres números
    suma = num1 + num2 + num3
    print(f"El primer número no es negativo. La suma de los tres números es: {suma}")
