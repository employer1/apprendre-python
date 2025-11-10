import math

nombre = float(input("Entre un nombre : "))

if nombre < 0:
    print("La racine carrée de ce nombre ne peut pas être calculée.")
else:
    racine = math.sqrt(nombre)
    print(f"La racine carrée de {nombre} est {racine:.2f}")