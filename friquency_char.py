st=input("Enter the string:")
a=""
for i in st:
  if i not in a:
    a=a+i
    c=st.count(i)
    print(i,"=",c)