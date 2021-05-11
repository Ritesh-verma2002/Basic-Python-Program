n=int(input("Enter the number of elements in set:"))
s=set()
for i in range(n):
    a=int(input())
    s.add(a)

item=(int(input()))
print(s)
if item in s:
    s.remove(item)
    print(s)