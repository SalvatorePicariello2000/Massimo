i=0
c=input("Inserisci il primo numero")
c=int (c)
while i<9:
	m=input ("Inserisci un altro numero")
	m=int (m)
	if c<m:
		c=m
	i+=1
print (c)