i=int(input())
j=int(input())

m=[]
n=[]
for a in range(i):
    ls=[]
    for b in range(j):
       ls.append(int(input()))
    m.append(ls)
print(m)
for a in range(i):
    for b in range(j):
        print(m[a][b],end=" ")
    print("")
for a in range(i):
    ls1=[]
    for b in range(j):
       ls1.append(int(input()))
    n.append(ls1)
print(n)

for a in range(i):
    for b in range(j):
        print(n[a][b],end=" ")
    print("")
res=[]
for a in range(i):
    re=[]
    for b in range(j):
        r=m[a][b]+n[a][b]
        re.append(r)
    res.append(re)
print("resultant matrix is:")
for a in range(i):
    for b in range(j):
        print(res[a][b],end=" ")
    print()