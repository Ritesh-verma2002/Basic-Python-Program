def fact(i):
    pro=1
    while i>0:
        pro=pro*i
        i=i-1
    return pro
a=int(input("Enter the number:"))
print("The factorial=",fact(a))
