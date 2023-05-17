
"""
    GENERATOR COMPREHENSION

is like a list comprehension, but instead of finding all the items
it waits, and yields each item one by one
 only difference is that they don’t allocate memory for the whole list but generate one item at a time

generator comprehension is the lazy version of a list comprehension
"""
from sys import getsizeof


list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
gener_comp = (x ** 2 for x in range(10) if x % 2 == 0)

print(id(list_comp))
print(id(gener_comp))

# for i in gener_comp:
#     print(i)

print(getsizeof(list_comp))
print(getsizeof(gener_comp))

"""
next
return?
throw?
"""
