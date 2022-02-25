# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and #3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
i = 0
for x in range(2000, 3201):
    if(x % 7 == 0) and (x % 5 != 0):
        print(f'{x}', end=',')
        i += 1
print("\b")
print(f'Total Number of Numbers divisible by 7 and not multiple of 5 {i}')

# python 2 and string
l = []
for x in range(2000, 3201):
    if(x % 7 == 0) and (x % 5 != 0):
        l.append(str(x))
print(','.join(l))
