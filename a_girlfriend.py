n = int(input("Enter a boyfriend's coordinate:"))
count = 0
i=5
if n<=15:
  while i>=1:
      while n > 0:
          t = n-i
          if t >=0:
              count = count + 1
              n = t
          i=i-1
  print("Boyfriend has to move",count,"steps")
else:
    print("Invalid boyfriend's Coordinate!!!!")




