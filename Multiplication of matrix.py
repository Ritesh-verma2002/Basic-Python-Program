x=int(input("enter rows:"))
y=int(input("enter column:"))
m=[]
n=[]
print("enter first matrix")
for i in range(x):
    a = []
    for j in range(y):
        p=int(input())
        a.append(p)
    m.append(a)
print(m)
"""for i in range(x):
    for j in range(y):"""
        #print(m)
print("enter second matrix")
for i in range(x):
    a = []
    for j in range(y):
        p=int(input())
        a.append(p)
    n.append(a)
print(n)
result=[]

for i in range(len(m)):
    f = []

    for j in range(len(n[0])):
        w = 0
        for k in range(len(n)):
            w += m[i][k] * n[k][j]
        f.append(w)
    result.append(f)
print("Multiplication of matrix= ")
for a in range(x):
    for b in range(y):
        print(result[a][b],end=" ")
    print()

