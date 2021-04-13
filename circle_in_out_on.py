print("Enter the center points of circle:")
x1=int(input())
y1=int(input())
radius=int(input("Enter the radius of circle"))
print("Enter the co_ordinate of point:")
x2=int(input())
y2=int(input())
dis=((x2-x1)**2+(y2-y1)**2)**0.5
if dis==radius:
    print("point is on the circle")
elif dis<radius:
    print("point is inside the circle")
else:
    print("point is out side the circle")