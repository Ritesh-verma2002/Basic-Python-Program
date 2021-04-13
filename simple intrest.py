p=int(input("enter principal amount:"))
r=eval(input("enter rate od intrest:"))
t=int(input("enter time duration:"))
si=p*r*t/100
ta=p*(1+(r*t))
print("the simple intrest is:",si)
print("the total amount is:",ta)
