data=[{'id':'1','sucess': True},{'id':'2','sucess': False},{'id':'3','sucess': True}]
count=0
for i in data:
        for j in i.values():
              if j==True:
                  count=count+1
print("The number of true Sucess:",count)
