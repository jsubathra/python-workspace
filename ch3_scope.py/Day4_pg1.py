# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Suppose the following input is supplied to the program:

class Divide7:
    def bySeven(self, n):
        for i in range(0, n+1):
            if i % 7 == 0:
                yield i


divisible = Divide7()
generator = divisible.bySeven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)
