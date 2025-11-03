chaine = "ceci est une chaine"
def fonction(chaine):
    nb = 0
    for i in range(len(chaine)):
        if chaine[i].isspace():
            nb = nb + 1
    return nb + 1
print(fonction(chaine))