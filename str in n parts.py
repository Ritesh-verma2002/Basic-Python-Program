st=input("Enter the string-")
n=int(input("Enter the number of parts-"))
r=len(st)
t=int(r/n)
for i in range(0,len(st),t):
    f=st[i:i+t]
    print(f)