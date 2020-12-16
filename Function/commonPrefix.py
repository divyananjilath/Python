n=int(input())
a=[]
for i in range(n):
	a.append(input())
pre=a[0][0]
for i in range(n):
	if(a[i][0] != pre):
		pre = -1
		break
print(pre)
