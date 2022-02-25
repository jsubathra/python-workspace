# FILE OPEN READ
f = open('test.txt', 'r')  # r,w,r+(read write),a(append)
print(f.name + f.mode)
f.close()

# Context Manager
# File is closed automatically , no need to close seperately
with open('test.txt', 'r') as f:
    f_contents = f.read()  # read everything
   # f_contents = f.readlines() # returns a list with file contents with new line added
   # f_contents = f.readline() # Line by Line
   # print(f_contents)

with open('test.txt', 'r') as f:
    for line in f:
        pass
        # print(line) # It gives the extra line between
        # print(line, end='')  # No extra space

with open('test.txt', 'r') as f:
    # f_contents = f.read(100)  # read first 100 char
    size_to_read = 10
    f_contents = f.read(size_to_read)  # read first 10 char
    while(len(f_contents) > 0):
        print(f.tell())  # current position in the file

        print(f_contents, end='/')
        f_contents = f.read(size_to_read)

    # seek method
with open('test.txt', 'r') as f:
    # f_contents = f.read(100)  # read first 100 char
    size_to_read = 10

    f_contents = f.read(size_to_read)  # read first 10 char
    print(f_contents, end='*')

    # used to manipulate the current position in the file - 0 means start
    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)


# print(f.closed) # returns True as file is closed
# print(f.read()) # Cannot read as it is outside the context manager
