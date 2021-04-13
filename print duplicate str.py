st=input("Enter the sring:")
k=[]
b=st.split()
for i in b:
    if b.count(i)>1 and i not in k:
        k.append(i)
print(" ".join(k))