dict ={
    "Tanya":13,
    "Ritesh":20,
    "Gudda":16
}
dict1 = {}
k = sorted(dict,key=dict.get)


for i in k:
    dict1[i] = dict[i]

print(k)