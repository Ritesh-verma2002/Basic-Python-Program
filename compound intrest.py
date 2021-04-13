p=int(input("Enter Principal intrest:"))
r=eval(input("Enter rate of intrest:"))
t=int(input("Enter the time:"))

ta=p*((1+r/100)**t)
ca=ta-p
print("coumpound intrest is:",'%.2f'%ca)
print("total amount is:",ta)
