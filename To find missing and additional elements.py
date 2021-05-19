list1 = [11, 12, 13, 14, 15, 16]
list2 = [14, 15, 16, 17, 18]
print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))
print("Missing values in first list:", (set(list2).difference(list1)))
print("Additional values in first list:", (set(list1).difference(list2)))