def remplir_dictionnaire():
    """Remplit le dictionnaire des copains avec leurs âges et tailles."""
    copains = {}

    print("=== Remplissage du dictionnaire ===")
    while True:
        nom = input("Entrez le nom du copain (ou 'stop' pour terminer) : ").strip()
        if nom.lower() == "stop":
            break

        try:
            age = int(input(f"Entrez l'âge de {nom} (en années) : "))
            taille = float(input(f"Entrez la taille de {nom} (en mètres, ex: 1.75) : "))
            copains[nom] = (age, taille)
            print(f"{nom} ajouté avec succès !\n")
        except ValueError:
            print("⚠️ Données invalides. Recommencez.\n")

    return copains


def consulter_dictionnaire(copains):
    """Permet de consulter les informations dans le dictionnaire."""
    print("\n=== Consultation du dictionnaire ===")
    while True:
        nom = input("Entrez le nom à rechercher (ou 'stop' pour terminer) : ").strip()
        if nom.lower() == "stop":
            break

        if nom in copains:
            age, taille = copains[nom]
            print(f"Nom : {nom} - âge : {age} ans - taille : {taille:.2f} m")
        else:
            print(f"⚠️ {nom} n'est pas dans le dictionnaire.")


# --- Programme principal ---
if __name__ == "__main__":
    base_copains = remplir_dictionnaire()
    consulter_dictionnaire(base_copains)