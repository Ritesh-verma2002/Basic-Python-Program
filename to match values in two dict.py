d1={'key1':1,'key2':2,'key':3}
d2={'key1':1,'key2':3}
for i,j in d1.items():
      if i in d2.keys() and j in d2.values():
          print(i,": is present in both x and y")