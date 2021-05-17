l1=['a','b','c','d']
l2=[1,2,2,4]
d={}
for i in range (len(l1)):
    j=i
    d[l1[i]]=l2[j]
print(d)