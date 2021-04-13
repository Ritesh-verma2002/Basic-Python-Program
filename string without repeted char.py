st=input("Enter the string:")
a=""
for i in st:
  if i not in a:
    a=a+i
print("String without repeated words is ",a)