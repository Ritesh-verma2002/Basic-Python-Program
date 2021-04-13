st=input("Enter the string-")
num=""
a=st.split()
for i in range(0,len(a)):
    if len(a[i])>len(num):
        num=a[i]
print("The largest word is-", num)





