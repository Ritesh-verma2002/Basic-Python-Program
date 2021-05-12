n=int(input("Enter the number of elements in set:"))
s=set()
for i in range(n):
    a=int(input())
    s.add(a)
l=list(s)
lst=[]
print(l)
num=0
for i in l:
    for j in l:
        if i*j>num:
            num=i*j
            lst.append(num)
lst=sorted(lst)

print("The two largest product is:",lst[-1],lst[-2] ," by",l[-1],l[-2])
