l = [1, 2, 3, 2, 4, 5, 1, 5, 6, 9, 7, 8, 5]

def func(l):
    l2 = []
    for i in l:
        if i in l2:
            continue
        else:
            l2.append(i)
        l.sort()
    return l2

print(func(l))