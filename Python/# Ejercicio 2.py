# Ejercicio 2
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

# Para la división, controlamos que num2 no sea 0
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir por 0"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")
print(f"División: {division}")
