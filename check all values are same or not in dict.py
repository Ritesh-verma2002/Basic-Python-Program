dict = {"Gfg": 5, "is": 5, "Best": 5}
print("The original dictionary is : " + str(dict))
res = len(list(set(list(dict.values())))) == 1
print("Are all values similar in dictionary? : " + str(res))