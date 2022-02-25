# Dictionary --- key value pairs
# Syntax is curly braces seperated by comma key and values with colon
student = {'name': 'Suba', 'age': '38', 'courses': ['Art', 'MAth']}
print(student)  # print the entire dictionary

# Get only the value for the key name and the key can be any data type
print(student['name'])
# print(f"Gives Key Error {student['phone']}")
print(f" Will return None if no key present :  {student.get('Phone')}")
print(
    f" can assign value also if key not present :  {student.get('Phone','NotFound')}")
student['phone'] = ['555-55555']  # Add new key value
student['name'] = 'Jane'  # Update existing key to a new value
print(student)  # new

# Dict inside the method
student.update({'name': 'Suba', 'age': '35', 'phone': '555-5655'})
print(f'Dict with multiple updated key values {student}')

# Delete key value
del student['age']
print(f'Dict with age deleted: {student}')
# Also can delete with pop method and get the value deleted and delete the value corresponding to the key
pop_phone = student.pop('phone')
print(f'Popped value from the dict : {pop_phone}')
print(f'After popped the dict will be : {student}')

# access key and values
print(f'count of the keys in the Dict: {len(student)}')
print(f'get the keys in the Dict: {student.keys()}')
print(f'get the values in the Dict: {student.values()}')
print(f'get the all the items in the Dict: {student.items()}')

# loop through the dict
for key in student:
    # this will just give only the key names and not the values
    print(f'Only key printed : {key}')

for key, value in student.items():
    print(f'Key: {key}')
    print(f'Value: {value}')

for value in student.values():
    print(value)
