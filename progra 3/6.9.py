longueur1 = int(input("Longueur 1: "))
longueur2 = int(input("Longueur 2: "))
longueur3 = int(input("Longueur 3: "))

# calculer longueur
if longueur1 == longueur2 and longueur3 == longueur1:
    print("triangle équilatéral ", end="")
elif longueur1 == longueur2 or longueur1 == longueur3 or longueur2 == longueur3:
    print("triangle isocèle ", end="")
else:
    print("triangle quelconque ", end="")

# calculer rectangle
if longueur1 ** 2 == longueur2 ** 2 + longueur3 ** 2:
    print("et rectangle")
elif longueur2 ** 2 == longueur1 ** 2 + longueur3 ** 2:
    print("et rectangle")
elif longueur3 ** 2 == longueur1 ** 2 + longueur2 ** 2:
    print("et rectangle")
else:
    print("qui n'est pas rectangle")