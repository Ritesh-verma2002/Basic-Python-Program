d={'math':81,'physics':53,'chemstry':61}
s=sorted(d.values())
t=s[::-1]
print(t)
k=list(d.keys())
c=list(d.values())
n=0
while(n<3):
   p=c.index(t[n])
   print(k[p],":", d.get(k[p]),end=" ")
   #to get the key by its value
   n=n+1