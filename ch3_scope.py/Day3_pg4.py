# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
input_str = input("Enter the Deposit and Withdrawal").split(' ')
D, W = '', ''
Amt = 0
input_list = []
input_list.append(input_str)
print(input_list)
for item in input_list:
    print(item)
    # if 'D' in item:
    #     Amt += int(item.remove('D '))
    # elif 'W' in item:
    #     Amt -= int(item.remove('W '))
print(Amt)
