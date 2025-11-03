longueur1 = int(input("longueur 1: "))
longueur2 = int(input("longueur 2: "))
longueur3 = int(input("longueur 3: "))

def volBoite(x1=10, x2=10, x3=10):
    return x1 * x2 * x3

print(volBoite(longueur1, longueur2))