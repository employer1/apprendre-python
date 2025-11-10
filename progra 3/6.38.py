jour = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Decembre']

for i, x in enumerate(jour):
    mois.insert(2 * i + 1, x)

print(mois)