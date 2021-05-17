dict1 = { 't' : [1, 2, 3] , 'r' : [4, 5, 6] , 'tr' :[7, 8, 9]}
dict2 = {}
for key in dict1:
    dict2[key] = sum(dict1[key])
print(dict2)