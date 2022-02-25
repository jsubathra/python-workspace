# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the program:

# Hello world
# Practice makes perfect
input_str = "Hello world\nPractice makes perfect"
print(input_str.upper())

# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again
input_str1 = "hello world and practice makes perfect and hello world again"
input_list = input_str1.split(' ')
input_list.sort()
for i in input_list:
    if (input_list.count(i) >= 1):  # if word occurance is there then it will return count >1ß
        input_list.remove(i)

print(','.join(input_list))

# Binary input
input_int = "0100,0011,1010,1001"
input_intlist = input_int.split(',')
for i in input_intlist:
    if(int(i, 2) % 5 == 0):  # int(i,2) -- converts binary to int
        print(i)

# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
l = []
for x in range(1000, 3001):
    if(x % 2 == 0):
        l.append(str(x))

# print(l)
print(','.join(l))
