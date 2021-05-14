s=input("Enter the string:")
se=set()
n=int(input("no. of Element"))
for i in range(n):
    b=input()
    se.add(b)
se=list(se)
num=0
for i in se:
    if i==s:
        num=num+1
if num>0:
        print("String present")
else:
        print("String not present")