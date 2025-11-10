t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
t3=[]
for i in range(len(t1)):
    t3.append(t1[i])
    t3.append(t2[i])
print(t3)