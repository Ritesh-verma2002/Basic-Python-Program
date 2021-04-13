st=input("Enter the string:")
a=0
c=0
b=0
v="aeiouAEIOU"
for i in st:
    if i in v:
        a=a+1
    elif i==" ":
        b=b+1
    else:
        c=c+1
print("Total vowels are-",a)
print("Total consonants are-",c)
print("Total white spaces are-",b)