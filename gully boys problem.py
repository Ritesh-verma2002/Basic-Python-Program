a=input()
p=int(input())
n=int(input())
b=a[p::] 
b=b+a[:p]
b=b.replace(" ","")
for k in range(n):
    for i in b:
        print(i,end=" ")