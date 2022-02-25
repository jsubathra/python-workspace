# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:a
input_str = "Hello Worldas 123"
# input_list = input_str.split(' ')
# output_dict = {}
# for x in input_list:
#     try:
#         int(x)
#         output_dict['digit'] = len(x)
#     except Exception as e:
#         if 'letters' not in output_dict.keys():
#             output_dict['letters'] = len(x)
#         else:
#             output_dict['letters'] += len(x)


# print(output_dict)

# letter, digit = 0, 0
# for i in input_str:
#     if ('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z'):
#         letter += 1
#     if '0' <= i and i <= '9':
#         digit += 1

# print("LETTERS {0}\nDIGITS {1}".format(letter, digit))

input_str = "HEllo Worldabc123"
digits, letter = 0, 0
for str1 in input_str:
    if str1.isalpha():
        digits += 1
    elif str1.isnumeric():
        letter += 1
print(f'Letters {letter} : Digits {digits}')

input_str = "Hello world!"
upper, lower = 0, 0
for str1 in input_str:
    upper += str1.isupper()
    lower += str1.islower()
print(f'Upper Case {upper} : LowerCase {lower}')
