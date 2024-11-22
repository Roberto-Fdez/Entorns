# Demanem els dos valors a l'usuari
valor1 = float(input("Introdueix el primer valor: "))
valor2 = float(input("Introdueix el segon valor: "))

# Identifiquem quin és el major i quin és el menor
if valor1 > valor2:
    major = valor1
    menor = valor2
else:
    major = valor2
    menor = valor1

# Verifiquem que el menor no sigui zero per evitar divisió per zero
if menor != 0:
    divisio = major / menor
    print(f"La divisió del major pel menor és: {divisio}")
else:
    print("Error: no es pot dividir per zero.")