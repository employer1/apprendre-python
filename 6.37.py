nom_jour = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
nom_mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']
j = 1
m = 1
s = 0
while m < 13:
    if j >= 29 and m == 1:
        j = 1
        m = m + 1
    elif j == 31 and (m == 3 or m == 5 or m == 8 or m == 10):
        j = 1
        m = m + 1
    elif j == 32:
        m = m + 1
        j = 1

    if s == 7:
        s = 0

    if m == 13:
        break

    print(nom_jour[s], j, nom_mois[m - 1])
    s = s + 1
    j = j + 1