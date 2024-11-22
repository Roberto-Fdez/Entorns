# Demanem els tres nombres a l'usuari
nombre1 = float(input("Introdueix el primer nombre: "))
nombre2 = float(input("Introdueix el segon nombre: "))
nombre3 = float(input("Introdueix el tercer nombre: "))

# Utilitzem la funció max() per trobar el major nombre
major = max(nombre1, nombre2, nombre3)

# Mostrem el nombre més gran per pantalla
print(f"El nombre més gran és: {major}")