student = {
  'name': 'tanya',
  'class': 'btech',
  'roll_id': '61'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'tanya'})
print(student.keys() >= {'roll_id', 'name'})