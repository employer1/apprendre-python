note = int(input("note: "))
total = int(input("total: "))
note = note / total * 100

if note < 40:
    print("E")
elif note < 50:
    print("D")
elif note < 60:
    print("C")
elif note < 80:
    print("B")
else:
    print("A")