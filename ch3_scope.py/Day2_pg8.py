# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# without,hello,bag,world

input_str = "without,hello,bag,world"
to_list = input_str.split(',')
to_list.sort()
print(','.join(to_list))
# sorted_input = sorted(input_str.split(','))
# print(sorted_input)
# print(to_sort.sort())
