def changeCar(ch, ca1, ca2, debut=0, fin=None):
    # Si fin n'est pas donné, on remplace jusqu'à la fin de la chaîne
    if fin is None:
        fin = len(ch)

    # On garde avant, on modifie le segment, on garde après
    avant = ch[:debut]
    segment = ch[debut:fin].replace(ca1, ca2)
    apres = ch[fin:]

    return avant + segment + apres

print(changeCar("banane en sueur", " ", "*"))

print(changeCar("banane au saumon qui sent pas la fraise parce que le frigo blanc ne permettait pas ça", " ", "*", 10, 40))