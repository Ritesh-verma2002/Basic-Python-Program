#copy()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.copy()
print("copy of dictionary",a)
#output: {'Name': 'Ritesh verma', 'Section': 'C', 'Roll number': 44}



#clear()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.clear()
print("clear full dictionary", a)
#output: clear full dictionary None


#fromkeys()
d={"Name":"Ritesh verma", "Section":"C","Roll number":44}
v=[1]
a=d.fromkeys(d,v)
print(a)
#output: {'Name': [1], 'Section': [1], 'Roll number': [1]}




#clear()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.clear()
print("clear full dictionary",a)
#output: clear full dictionary None




#get()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.get('Name')
print(a)
#output: Ritesh verma




#items()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.items()
print(a)
#output: dict_items([('Name', 'Ritesh verma'), ('Section', 'C'), ('Roll number', 44)])




#get()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.get('Name')
print(a)
#output: Ritesh verma




#keys()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.keys()
print(a)
#output: dict_keys(['Name', 'Section', 'Roll number'])





#popitem()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.popitem()
print(d,a)
#output: {'Name': 'Ritesh verma', 'Section': 'C'} ('Roll number', 44)




#setdefault()   .....EX-1
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.setdefault("verma")
print(d,a)
#output: {'Name': 'Ritesh verma', 'Section': 'C', 'Roll number': 44, 'verma': None} None



#setdefault()    .......EX-2
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.setdefault("years",18)
print(d,a)
#output: {'Name': 'Ritesh verma', 'Section': 'C', 'Roll number': 44, 'years': 18} 18




#pop()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.pop("Section")
print(d,a)
#output: {'Name': 'Ritesh verma', 'Roll number': 44} C




#values()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a=d.values()
print(d,a)
#output: {'Name': 'Ritesh verma', 'Section': 'C', 'Roll number': 44} dict_values(['Ritesh verma', 'C', 44])




#update()
d={"Name":"Ritesh verma","Section":"C","Roll number":44}
a={"age":18}
d.update(a)
print(d,a)
#output {'Name': 'Ritesh verma', 'Section': 'C', 'Roll number': 44, 'age': 18} {'age': 18}