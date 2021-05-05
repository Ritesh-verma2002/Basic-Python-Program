


n=int(input("enter the size"))
a=[]
for i in range(n):
    print(i)
    p=int(input("Enter the elements"))
    a.append(p)
print(a)
for i in range(n-1):
   for j in range(n-1):
       if a[j]>a[j+1]:
           t=a[j]
           a[j]=a[j+1]
           a[j+1]=t
print(a)