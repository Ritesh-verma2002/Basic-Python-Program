st1=input("Enter the string:")
k=[]
for i in st1:
    if i>='a'and i<='z' :
        if i in st1 and i not in k :
            k.append(i)
if len(k)==26:
    print("It is Pangram")
else:
    print("it is not Pangram")
