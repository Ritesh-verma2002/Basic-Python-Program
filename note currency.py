n=int(input("enter the amount:"))
n=n-100
      
a=n//2000
n=n-(2000*a)
b=n//500
n=n-(500*b)
c=n//100
c=c+1
x=f"""

100={c}
500={b}
2000={a}
"""
print(x)
