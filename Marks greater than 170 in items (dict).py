marks = {'Ritesh': 175,'Tanya': 180, 'Swastik': 165, 'Yash': 190}
print("Original Dictionary:")
print(marks)
print("Marks greater than 170:")
result = {key:value for (key, value) in marks.items() if value >= 170}
print(result)