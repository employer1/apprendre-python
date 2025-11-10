longueur1 = int(input("longueur 1: "))
longueur2 = int(input("longueur 2: "))
longueur3 = int(input("longueur 3: "))

def volBoite(*args):
    if len(args) == 1:
        # Cube : x^3
        x = args[0]
        return x * x * x

    elif len(args) == 2:
        # Prisme à base carrée : côté² * hauteur
        x, h = args
        return x * x * h

    elif len(args) == 3:
        # Parallélépipède : x1 * x2 * x3
        x1, x2, x3 = args
        return x1 * x2 * x3

    else:
        return "Erreur: tu dois donner 1, 2 ou 3 arguments."

print(volBoite(longueur1, longueur2, longueur3))