chaine = "ceci est une chaine de caractères"

def separer(chaine):
    positions = [-1]  # sentinelle avant le début
    for i, ch in enumerate(chaine):
        if ch.isspace():
            positions.append(i)
    positions.append(len(chaine))  # sentinelle fin

    mots = []
    for a, b in zip(positions, positions[1:]):
        segment = chaine[a+1:b]
        if segment:              # saute les segments vides si espaces multiples
            mots.append(segment)
    return mots

print(separer(chaine))