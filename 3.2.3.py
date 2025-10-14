l=[32,5,12,8,3,75,2,15]
x=0
for i in l[1:]:
    if i > x:
        x=i
print("le plus grand nombre est",x)
# ou: print("le plus grand nombre est",max(l))