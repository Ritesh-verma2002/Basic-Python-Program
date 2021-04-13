d=int(input("Enter the date:"))
m=int(input("Enter the month:"))
rm=12-m

if m==1 or m==3 or m==5 or m==7 or m==18 or m==10 or m==12:
    rd=31-d
elif m==2:
    rd=28-d
else:
    rd=30-d
td=rd+rm*30
print("the remaning days of the year is :",td)


