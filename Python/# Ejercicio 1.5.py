# Demanem el dia i el mes a l'usuari
dia = int(input("Introdueix el dia: "))
mes = int(input("Introdueix el mes (en número, 1-12): "))

# Comprovem si el mes és vàlid
if mes < 1 or mes > 12:
    print("Data incorrecta: el mes introduït no és vàlid.")
else:
    # Definim els dies màxims per a cada mes
    dies_per_mes = {
        1: 31,  2: 28,  3: 31,  4: 30,  5: 31,  6: 30,
        7: 31,  8: 31,  9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Obtenim el nombre màxim de dies per al mes introduït
    dies_maxim = dies_per_mes[mes]
    
    # Comprovem si el dia és vàlid per al mes donat
    if 1 <= dia <= dies_maxim:
        print("Data correcta.")
    else:
        print("Data incorrecta: el dia no és vàlid per al mes introduït.")