l = []
note = 0
while note >= 0:
    note = int(input("note: "))
    l.append(note)
    len(l)
    max = 0
    min = 100
    moy = 0
    i = 0
    for item in l:
        if l[i] > max:
            max = l[i]
        if l[i] < min:
            min = l[i]
        i = i + 1
        moy = moy + item
    print("maximum : ", max, "\nminimum : ", min, "\nmoyenne : ", moy / len(l))