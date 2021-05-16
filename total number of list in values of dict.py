d = {'A' : [1, 2],

        'B' : 3,

        'C' : 1,

        'D' : [7, 4] }
c=0
for x in d.values():
    if type(x)==list:
        c=c+1
print("The number of list in dictionary are:",c)