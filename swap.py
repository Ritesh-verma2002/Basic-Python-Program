a=eval(input("enter the first value:"))
b=eval(input("enter the second value:"))
x=f"""	Before swap:
		a={a}
		b={b}
	"""
print(x)
c=a
a=b
b=c
y=f"""	After swap:
		a={a}
		b={b}
	"""
print(y)

