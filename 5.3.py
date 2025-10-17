def cube(n):
	return n**3
def volume_sphere(r):
	return 4*3.1416*cube(r)/3

r=input("entrez la valeur rayon")
print("le volume de cette sphere vaut : ", volume_sphere(float(r)), "cm")