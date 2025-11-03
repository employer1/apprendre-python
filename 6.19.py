chaine = "Bonsoir je suis en c"
blocs = [chaine[i:i+5] for i in range(0, len(chaine), 5)]
blocs_inverses = blocs[::-1]
resultat = ''.join(blocs_inverses)
print(resultat)