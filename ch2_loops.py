# For Loops
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(f'Value is each {num}')

for num in nums:
    if num == 3:  # See the colon
        print('Found')
        break  # if condition met it will exit the loop and if we need to ignore the condition use continue
    print(num)  # See the indention


for num in nums:
    for letter in 'abc':  # Nested loops
        print(f' Nested Loop {num}, {letter}')


for i in range(10):  # loop only to run specific number of times
    # if range to start from 1 then use range(1,11)
    print(f'Loop for a range {i}')


# While Loop
x = 0
while x < 10:  # Endless loop untill condition met so increment is needed so can use while  True: , but have to use break
    print(f'While Loop: {x}')
    # if(x == 5):
    #   break
    x += 1

# can use break
