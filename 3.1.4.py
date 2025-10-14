msg="ceci est une chaîne de caractères"
msg2=""
for i in range(len(msg)-1,-1,-1):
    msg2+=msg[i]
print(msg2)