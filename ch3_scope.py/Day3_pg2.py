# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
a = '9'
sum = 0
n1 = int(a)
n2 = int(a+a)
n3 = int(a+a+a)
n4 = int(a+a+a+a)
sum = n1 + n2 + n3 + n4
print(f'Sum of 9 as a+aa+aaa+aaaa is {sum}')
