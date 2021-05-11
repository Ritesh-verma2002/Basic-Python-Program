a=input("Enter first String:")
b=input("Enter second String:")
x=set(a)
y=set(b)
c=x-y
d=y-x
c.update(d)
print("The letters are in two string but not in both:")
for i in c:
    print(i)
