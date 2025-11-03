chaine = "je suis très bête d'avoir été la"
def fonction(chaine):
    nb = 0
    for i in range(len(chaine)):
        if chaine[i] == "e" or chaine[i] == "é" or chaine[i] == "è" or chaine[i] == "ê" or chaine[i] == "ë":
            nb = nb + 1
    return nb
print(fonction(chaine))