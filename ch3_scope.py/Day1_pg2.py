# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# 1*2*3...*8
# x = 9
x = int(input())
fib = 1
for i in reversed(range(1, x+1)):
    fib *= i
print(fib)
