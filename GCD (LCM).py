a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    x=b
else:
    x=a
for i in range(1,x+1):
    if((a%i==0)and(b%i==0)):
        ans=i
print("the GCD of two number is:",ans)