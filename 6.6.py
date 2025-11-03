borne1 = int(input("borne 1: "))
borne2 = int(input("borne 2: "))
i = borne1
total = 0
while i <= borne2:
    if i % 5 == 0 or i % 3 ==0:
        total = total + i
    i = i + 1
print(total)