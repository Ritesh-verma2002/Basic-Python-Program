n=int(input("Enter the number:"))
a=1
for i in range(n+1):
    b = a
    a = a * 2
    for j in range(i+1):
        print(b,end="  ")
        b=b//2
    print("")