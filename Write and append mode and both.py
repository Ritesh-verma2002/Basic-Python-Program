# Write() function

f=open("datafile.txt","w")      #update old file or create new one
f.write("Ritesh and tanya are best friends")    #write in file
f.close()

#append() mode

f=open("datafile.txt","a")      #update old file or create new one
f.write("Ritesh and tanya are best friends")    #append in old file
f.close()


#read and write mod both

f=open("datafile.txt","r+")   #file open in read and write modes  both
print(f.read())
f.write("Ritesh and tanya are best friends")    #append in old file
f.close()

