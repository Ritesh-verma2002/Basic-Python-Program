n=int(input("Enter the number of elements in set:"))
s=set()
for i in range(n):
    a=int(input())
    s.add(a)
n=int(input("Enter the number of elements in set:"))
sub=set()
for i in range(n):
    b=int(input())
    sub.add(b)

if sub.issubset(s):
    print("The subset is present in set")
else:
    print("subset is not present in set")