l = [1, 2, 3, 4, 5]
def eleMax(liste, debut=0, fin=None):
    if fin is None:
        fin = len(liste)
    sous_liste = liste[debut:fin]
    max = sous_liste[0]
    for item in sous_liste:
        if item > max:
            max = item
    return max
print(eleMax(l, 1, 4))
