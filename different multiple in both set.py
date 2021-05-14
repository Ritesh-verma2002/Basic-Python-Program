n=int(input("Enter the number of elements in list-1:"))
s=set()
for i in range(n):
    a=int(input())
    s.add(a)
n=int(input("Enter the number of elements in list-2:"))
q=set()
for i in range(n):
    b=int(input())
    q.add(b)
n=int(input("Enter any number:"))
s=list(s)
q=list(q)
x=[]
y=[]
for i in s:
    if i%n==0:
        x.append(i)
for i in q:
    if i%n==0:
        y.append(i)
x=set(x)
y=set(y)
print(y^x)