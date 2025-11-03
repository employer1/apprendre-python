def trouverIndice(chaine="", caractere=""):
    if chaine == "" or caractere == "":
        return "erreur"
    nb = 0
    for i in range(len(chaine)):
        if chaine[i] == caractere:
            nb = nb + 1
    return nb
print(trouverIndice("Bonsoir, je suis très impatient de commencer", "e"))