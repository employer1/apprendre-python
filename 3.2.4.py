l1=[32,5,12,8,3,75,2,15]
l2=[]
l3=[]
for i in range(len(l1)):
    if l1[i] % 2 == 0:
        l2.append(l1[i])
    else:
        l3.append(l1[i])
print(l1,l2,l3)