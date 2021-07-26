N,M = list(input().split('x'))
a=int(N)
b=int(M)
c=0
for i in range(a):
    for j in range(b):
        if (i+j)%2!=0:
            c=c+1
print(c)
 //to count empty block in matrix