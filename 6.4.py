distance = int(input("quel est la distance en miles (par heure) :"))
vitesse = (distance * 1609.3) / 1000
print("vitesse : ", vitesse, " km/h")
print(f"vitesse : {vitesse/3.6:.2f} m/s")