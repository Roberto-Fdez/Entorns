# Ejercicio 3
num1 = float(input("Introduce el número 1: "))
num2 = float(input("Introduce el número 2: "))

if num1 > num2:
    print(f"El {num1} es mayor que el {num2}")
elif num1 < num2:
    print(f"El número {num2} es mayor que {num1}")
else:
    print(f"Ambos números son iguales: {num1} y {num2}")