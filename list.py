"""
Comprehension provides a precise way of writing a program in Python.
It reduces the code size without affecting its easy readability.

- List Comprehension
- Dictionary Comprehension
- Set Comprehension
- Generator Comprehension
"""
""" 
    LIST COMPREHENSION
(short way to create a new list)
    
     Output      Collection          If this condition
     Do this     For this            In this situation
    [  x + 1   for x in a_list     if x % 2 == 0   ]    
"""

a_list = [2, 7, 5, 8, 9, 4, 12]

""" with single If condition """
# # new_list = []
# for x in a_list:
#     if x % 2 == 0:
#         new_list.append(x + 1)
# # print(new_list)

# new_list = [x + 1 for x in a_list if x % 2 == 0]
# print(new_list)




""" nested if condition """
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list = []
# for x in b_list:
#     if x > 4:
#         if x % 2 == 0:
#             new_list.append(x)
# print(new_list)
#
# new_list = [x for x in b_list if x > 4 if x % 2 == 0]
# print(new_list)

""" with multiple If and Else conditions"""
c_list = [2, 4, 'Three', 5, 'Six', 7, 8, [1, 2]]
#
# new_list = []
# for x in c_list:
#     if type(x) != int:
#         new_list.append(x)
#     elif x % 2 == 0:
#         new_list.append('Even')
#     else:
#         new_list.append('Odd')
#
# print(new_list)
#
new_list = [x if not isinstance(x, int) else "Even" if x % 2 == 0 else "Odd" for x in c_list]
print(new_list)

""" with a nested For Loop """
d_list = [1, 2, 3]
e_list = [3, 2, 1]

new_list = []
for x in d_list:
    for y in e_list:
        new_list.append((x, y))

print(new_list)

new_list = [(x, y) for x in d_list for y in e_list]
print(new_list)


""" 
- is generally more compact and faster than normal functions and loops for creating list
- we should avoid writing very long list comprehensions in one line
- every list comprehension can be rewritten in for loop, 
    but not every for loop can be rewritten in the form of list comprehension
"""

""" before list comprehension"""
map()