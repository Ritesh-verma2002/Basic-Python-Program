n=int(input("Enter the number of elements in list-1:"))
s=[]
for i in range(n):
    a=int(input())
    s.append(a)
n=int(input("Enter the number of elements in list-2:"))
q=[]
for i in range(n):
    b=int(input())
    q.append(b)
n=int(input("Enter the number of elements in list-3:"))
r=[]
for i in range(n):
    c=int(input())
    r.append(c)
s=set(s)
q=set(q)
r=set(r)
x=s.intersection(q)
y=r.intersection(x)
aa=list(y)
pp=1
for i in aa:
  pp=pp*i

print("The product of elements comman in all three set are:",pp)
