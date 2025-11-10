chaine = "5"
def estUnChiffre(chaine):
    for i in range(len(chaine)):
        if  chaine[i].isdigit():
            digit = True
        elif not chaine[i].isdigit():
            return False
    return digit
print(estUnChiffre(chaine))