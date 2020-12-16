a=input()
a1=''
words=a.split()
for i in words:
	b=i[0].upper()
	a1=a1+b
	for j in range(1,len(i)):
		a1=a1+i[j]
print(a1)
