import math as m
a = int(input())
b = int(input())
i = round((m.degrees(m.atan(a/b))))
print(str(i)+u"\N{DEGREE SIGN}")