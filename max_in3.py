a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b:
    if a>c:
        print(a,"is greater number")
    else:
        print(c,"is greater number")
elif b>c:
    print(b,"is greater number")
else:
 print(c,"is greater number")