msg="y a-t-il la lettre e ?"
x=False
for i in msg:
    if i=="e":
        x=True
        break

if x == False:
    print("il n'y a pas de e dans cette chaîne de caractères")
else:
    print("il y a un e dans cette chaîne de caractères")