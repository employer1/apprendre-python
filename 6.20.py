def trouverIndice(chaine="", caractere=""):
    if chaine == "" or caractere == "":
        return -1
    for i in range(len(chaine)):
        if chaine[i] == caractere:
            return i
        elif i == len(chaine):
            return -1
print(trouverIndice("Bonsoir, je suis très impatient de commencer", "e"))