majuscule = "E"
def estUneMaj(chaine):
    for i in range(len(chaine)):
        if chaine[i].isupper():
            return True
        else:
            return False
print(estUneMaj(majuscule))