
m=[]
for i in range(4):
    a = []
    for j in range(4):
        p=int(input("enter the digit"))
        a.append(p)
    m.append(a)
for i in range(4):
    for j in range(4):
        print(m[i][j],end="  ")
    print("")
z=1
for i in range(4):
     for j in range(4):
        if m[j][i]!=m[i][j]:
            z=2
if z==1:
    print("Symmetric matrix")
else:
    print("Not Symmetric matrix")