l1=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
l2=[]
l3=[]
for i in range(len(l1)):
    if len(l1[i])>6:
        l2.append(l1[i])
    else:
        l3.append(l1[i])
print(l1,l2,l3)