"""
    SET COMPREHENSION

(a concise way to create a new set based on existing iterable(s))

        {iterator   for iterator  in sequence}
"""

numbers = [2, 4, 3, 4, 5, 6, 5]
unique_squares = {n * n for n in numbers}
# print(unique_squares)


unique_squares = set()
for n in numbers:
    unique_squares.add(n*n)
# print(unique_squares)


simpsons = 'Homer Simpson is son of Abraham Simpson and Father of Bart Simpson'
words = simpsons.split()

simpsons_set = {word for word in words if len(word) > 4}
# print(simpsons_set)
# print(set(words))

""" with if condition """
num_set = {12, 4, 56, 3, 45, 67, 89, 1, 6}

set_comprehension = {i for i in num_set if i > 25}
# print(num_set)
# print(set_comprehension)


car_set = {'Audi', 'Ford', 'Seat'}
lower_car = {car.lower() for car in car_set if car != 'Ford'}

print(lower_car)


