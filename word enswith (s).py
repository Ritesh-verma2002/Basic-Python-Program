st=input("Enter the string:")
b=st.split()
print("The words ends with 's'are-")
for i in range(0,len(b)):
    if b[i].endswith('s'):
        print(b[i])


