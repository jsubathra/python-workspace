import os
print(os.path)
try:
        f = open('ToDo.txt')
        f = open('currupt_file.txt')
    # var = bad_var # If this exception occurs then else part will not work
    if f.name == 'currupt_file.txt':
        # Raise Exception on your own
        raise Exception('Cannot read currupt file')
except FileNotFoundError as e:  # More specific exception
    print('Sorry! File does not Exist', e)
except Exception as e:
    print('Name Error: ', e)
else:  # After try and no exception control will come to else
    print(f.read())
finally:  # If try or exception it will come here
    f.close()
    print('In Finally')
