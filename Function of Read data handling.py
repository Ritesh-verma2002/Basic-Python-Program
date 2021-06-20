#read file by default
f=open("datafile.txt")
r=f.read()
print(r)
f.close()



#readline function
f=open("datafile.txt")
r=f.readline()      #this function read single line
print(r)
r=f.readline()      #this function read single line
print(r)
f.close()



#readlines() Function

f=open("datafile.txt")
r=f.readlines()     #store all lines in list
print(r)
f.close()

