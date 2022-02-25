# Tuples is immutatble - cannot change - only loop and access but not change
tuple_1 = ('Hist', 'Art', 'Phy', 'Comps')  # LIsts have [] but tuple has ()
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art' # are immutable - gives error but this can be done in lists and the new list will have the changed values
# print(tuple_1)
# print(tuple_2)

# Sets - cannot have duplicates
set_1 = {'Hist', 'Art', 'Phy', 'Comps', 'Art'}
print(set_1)
print('Art' in set_1)  # more optimized than list and tuples
set_2 = {'Hist', 'Art', 'Music', 'Dance'}
print(f' Common to both sets {set_1.intersection(set_2)}')
print(f' Present in set1 but not in set2 to {set_1.difference(set_2)}')
print(f' All in set1 and set2 {set_1.union(set_2)}')


# Empty lists
empty_ls = []
empty_ls = list()

# Empty tuple
empty_tp = ()
empty_tp = tuple()

# Empty Sets
empty_set = {}  # This is not right , Its dict
empty_set = set()
