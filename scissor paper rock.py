s1=input()
s2=input()
m1=input()
m2=input()
if m1=="Rock" and m2=="Scissor":
    print(s1,"Win")
elif(m1=="Rock" and m2=="paper"):
    print(s2,"Win")
elif(m1=="Paper" and m2=="Rock"):
    print(s1,"Win")
elif(m1=="Scissor" and m2=="Rock"):
     print(s2,"Win")
elif(m1=="Scissor" and m2=="Paper"):
    print(s1,"Win")
else:
    print(s2,"Win")