# Lists - can have duplicates , index, value, no definite length
courses = ["Hist", "Math", "Sci", "CompSci"]

#Len and Index
print(courses)
print(len(courses))
print(courses[-1])
# [0] - first ,[1:] -from 1st to last ,[-1] - last ,[4] - index error

# Add Items
courses.append("ART")  # Add to the last of the list
print(courses)
courses.insert(3, "Music")  # Add at any particular index
print(courses)
courses_2 = ["PE", "Dance"]
# courses.insert(0, courses_2)  # if a list is to be inserted Will be in the index as Sub list
print(courses)
courses.extend(courses_2)  # Only the values are inserted
print(courses)

# remove
courses.remove("Math")  # only removes the list value - not the index position
print(courses)
# By default only last element of the list -- Also we can grab the value it return
popped = courses.pop()
print(popped)
print(courses)

# Reverse

courses.reverse()  # reverse the items in the list with index positions
print(courses)
courses.sort()  # Alphabetical
print(courses)
courses.sort(reverse=True)  # Reverse Alphabeticall
print(courses)
num = [1, 4, 2, 5, 3]
num.reverse()
print(f'List reverse {num}')
num.sort()
print(f'List sort {num}')
num.sort(reverse=True)
print(f'List sort desc {num}')

print(sorted(courses))  # Will return a sorted new list

#min ,max and sum
print(
    f'Min of num is {min(num)}, Max of num is {max(num)} , Sum of num is {sum(num)}')
# Index of the value and is value not in list we wil get value Error
print(courses.index('CompSci'))
print('Art' in courses)  # Checks if Art contained in the list - Trur or False
for item in courses:
    print(f' Item in the list {item}')  # each item in the list is print

for index, item in enumerate(courses):  # enumerates return index and the value
    print(f' Item in the list with index {index},{item}')

# enumerates return index and the value with start position as 1
for index, item in enumerate(courses, start=1):
    print(f' Item in the list with index {index},{item}')

# Comma seperated
courses_str = ', '.join(courses)
print(courses_str)

# string back to list
new_courses = courses_str.split(', ')
print(new_courses)
