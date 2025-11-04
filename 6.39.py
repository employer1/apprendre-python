import random

# Liste des valeurs possibles
valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]

# Liste des couleurs possibles
couleurs = ["Trèfle", "Carreau", "Cœur", "Pique"]

print("Appuie sur Entrée pour tirer une carte (ou tape 'q' pour quitter).")

while True:
    choix = input("> ")
    if choix.lower() == "q":
        print("Fin du jeu.")
        break

    valeur = random.choice(valeurs)
    couleur = random.choice(couleurs)

    print(f"{valeur} de {couleur}")