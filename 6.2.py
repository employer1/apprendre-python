l=[1]
i=1

while i < 11:
    l.append(l[i-1]+l[i-2])
    print(l[i-1])
    i=i+1