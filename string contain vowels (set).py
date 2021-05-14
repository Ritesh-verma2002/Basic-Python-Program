n=int(input("Enter the number of elements in set:"))
s=set()
for i in range(n):
    a=input()
    s.add(a)
l=list(s)
res=set()
v=["a","i","o","e","u"]
for i in l:
    i=i.casefold()
    for j in v:
        if j in i:
            res.add(i)
print("The string which contain vowels=",res)