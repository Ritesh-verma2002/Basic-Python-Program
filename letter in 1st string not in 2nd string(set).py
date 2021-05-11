a=input("Enter first String:")
b=input("Enter second String:")
x=set(a)
y=set(b)
c=x-y
print("The letters which is in first string not in second string:ta")
for i in c:
    print(i)
