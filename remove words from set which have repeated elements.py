se=set()
n=int(input("no. of Element"))
for i in range(n):
    b=input()
    se.add(b)
se=list(se)
a=[]
c=0
for i in se:
    c=0
    for j in i:
        c=c+(i.count(j))
    if c==len(i):
        a.append(i)
print(set(a))