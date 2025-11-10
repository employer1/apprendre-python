def trouverIndice(chaine="", caractere="", debut =0):
    if chaine == "" or caractere == "":
        return -1
    sous_chaine = chaine[debut:]
    for i in range(len(sous_chaine)):
        if sous_chaine[i] == caractere:
            return i
        elif i == len(sous_chaine):
            return -1
print(trouverIndice("Bonsoir, je suis très impatient de commencer", "e", 11))