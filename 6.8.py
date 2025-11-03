nom = input("votre nom: ")
sexe = "a"
while sexe != "M" and sexe != "F":
    sexe = input("votre sexe (M / F): ")
    if sexe != "M" and sexe != "F":
        print("votre sexe non valide")
if sexe == "M" or sexe == "m":
    print("Chère Monsieur", nom)
else:
    print("Chère Madame", nom)