chaine = "Ceci est une Chaine de caractères"

def extraire(chaine):
    l = []
    for i in range(len(chaine)):
        indice1 = 0
        indice2 = 0
        if chaine[i].isupper():
            indice1 = i
            for j in range(i, len(chaine)):
                if chaine[j].isspace():
                    mot = chaine[indice1:j]
                    l.append(mot)
                    break
    return l

print(extraire(chaine))