d={"a":9,"b":4,"c":6,"d":9}
a=list(d.items())
r={}
for key,value in d.items():
    if value not in r.values():
        r[key]=value
print(r)