
a = True
# if isinstance(a, float):
#     print(True)
# else:
#     print(False)
""" one line If"""
# print(True if isinstance(a, int) else False)

a_list = ['dog', 'cat', 'mouse', 'bird']
b_tuple = (25, 5, 1)

result = zip(a_list, b_tuple)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
