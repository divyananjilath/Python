n=input()
c1=0
c2=0
for i in n:
	if(i =='('):
		c1=c1+1
	elif(i == ')'):
		c2=c2+1
if(c1==c2):
	print("yes")
else:
	print("no")
