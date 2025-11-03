chaine = "Ceci est une Chaine de caractères"

def extraire(chaine):
    count = 0
    for i in range(len(chaine)):
        if chaine[i].isupper():
            count = count + 1
    return count

print(extraire(chaine))