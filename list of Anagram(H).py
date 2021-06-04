count=0

a=input()
b=input()
l=len(a)
l2=len(b)
a=a[2:l-2]
a=a.split("', '")
b=b[2:l2-2]
b=b.split("', '")
for i in a:
    for j in b:
        if sorted(i)==sorted(j):
            count=count+1
print(count)