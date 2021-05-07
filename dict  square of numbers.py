n= int(input())
d={}
for i in range(1,n+1):
    a={i:i**2}
    d.update(a)
print(d)