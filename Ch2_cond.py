condition = 'Test'

# By default the condition evaluates to True in the If
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

lang = 'Python'
# No Switch Case is here and if, elif and not elseif ..Note the colon at the end
if lang == 'Python':
    print('Lang is Python')
elif lang == 'Java':
    print('Lang is Java')
elif lang == 'JavaScript':
    print('Lang is JavaScript')
else:
    print('No Match')

# and , Or and not conditional
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Please log in again')

user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:  # any one condition
    print('Admin Page')
else:
    print('Please log in again')

# NOt : evaluates the condition to Not
logged_in = False
if not logged_in:
    print(f'Pls log in {logged_in}')
else:
    print('Good')

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


a = [1, 2, 3]
b = [1, 2, 3]
# both a and b have same elements so condition is true but id will be different
if a == b:
    print(id(a))
    print(id(b))
if a is b:  # checks if object identity is same
    print(a)
    print(b)

a = b  # when we assign then both the objects have same meme identity
if a == b:
    print(id(a))
    print(id(b))
if a is b:  # checks if object identity is same
    print(a)
    print(b)
