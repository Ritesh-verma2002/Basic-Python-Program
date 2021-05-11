n=int(input("Enter the number of elements in set-1:"))
s=set()
for i in range(n):
    a=int(input())
    s.add(a)
n=int(input("Enter the number of elements in set-2:"))
p=set()
for i in range(n):
    b=int(input())
    p.add(b)
print(p-s)