# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81
#input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
input_str = input("Enter the numbers: ").split(',')
input_list = [int(i) for i in input_str]
my_list = [n*n for n in input_list if n % 2 != 0]
print(my_list)
