import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
a=int(input("Enter the number of elements in set:"))
s=set()
for i in range(a):
    b=int(input())
    s.add(b)
n=int(input("Enter the order of pair:"))
print(findsubsets(s, n))