st=input("enter the string:")
print("Before--",st)
s=""
for i in st:
    if i.isalpha():
        s+=i
print("After --",s)