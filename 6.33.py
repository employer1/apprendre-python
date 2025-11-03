chaine = "Ceci est la PLUS grande chaine de code ASCII du MoNdE"

def convertir(chaine):
    chaine2 = ""
    for i in range(len(chaine)):
        if chaine[i].isupper():
            chaine2 = chaine2 + str.lower(chaine[i])
        else:
            chaine2 = chaine2 + str.upper(chaine[i])
    return chaine2

print(convertir(chaine))