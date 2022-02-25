import antigravity  # open a webbrowser
import os  # os files
import calendar  # isLeap
import datetime  # date
import math  # MAthematical operators
import random  # Import std library to be used to choose random course in courses
import my_module  # to import the whole module

import my_module as mm  # to import as alias and call using mm
from my_module import find_index  # import only the find_index function
# import the find_index function and test variable
from my_module import find_index, test

# import the find_index function and test variable with alias
from my_module import find_index as fi, test as t

from my_module import *  # Import all in the whole Module

import sys
courses = ['Math', 'Art', 'Science', 'CompSci']

index = my_module.find_index(courses, 'Science')

print(index)
print(test)
# dir that contains the script , python path env variable, std library , site pkg - 3rd party
print(sys.path)

# If the module is in diff path than the original script path
#import sys
#sys.path.append('/Users/subathrajanarthanam/Documents/py-workspace/<path of the file name>')

# Add below in env path
# nano ~/.bash_profile
# export PYTHON_PATH='/Users/subathrajanarthanam/Documents/py-workspace/<path of the file name>'
# restart the terminal
# python

# RANDOM COURSE CHOICE BY IMPORTING RANDOM LIBRARY
random_course = random.choice(courses)
print(f' RANDOM COURSE CHOICE {random_course}')


today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)  # this gives the path of the os.py file
