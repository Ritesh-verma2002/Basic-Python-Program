n=int(input("Enter the number of elements in set:"))
s=set()
for i in range(n):
    a=int(input())
    s.add(a)
print("The sum of max and min:",max(s)+min(s))