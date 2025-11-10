annee = int(input("annee: "))
if annee % 400 == 0 or annee % 4 == 0:
    if annee % 100 == 0:
        if annee % 400 == 0:
            print("bissextile")
        else:
            print("pas bissextile")