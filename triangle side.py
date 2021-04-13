a=int(input("enter first side:"))
b=int(input("enter second side:"))
c=int(input("enter third side:"))
if(a+b>c and a+c>b and b+c>a):
        if(a==b==c):
                print("It is equal triangle")
        elif(a==b or b==c or c==a):
                print("isoceled triangle")
        else:
                print("scalene triangle")

else:
	print("invalid triangle")

		
