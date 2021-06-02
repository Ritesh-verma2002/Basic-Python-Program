def fab(x):
    a = 0
    b = 1
    i = 0
    print(a)
    print(b)
    while i < x:
        c = a + b
        print(c)
        a = b
        b = c
        i = i + 1
x=int(input("Enter the number:"))
fab(x)
