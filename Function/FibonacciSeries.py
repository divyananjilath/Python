#Display fibonacci series, and store the values in a List
a=[0,1]
n=int(input())
for i in range(2,n):
  a.append(a[i-1]+a[i-2])
print(a)
